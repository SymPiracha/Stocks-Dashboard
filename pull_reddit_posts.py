import datetime
import time
import os
import os.path as osp
import requests
import json


# function used to write json to file
def write(posts, output_file):
    new_line_char = '\n'
    # append each post to a file
    with open(output_file, 'a') as file:
        for post in posts:
            # dump this dic as a json string in file
            json.dump(post, file)
            #print(post['title'])
            # append new line char
            file.write(new_line_char)

# pulls data and creates json for a specific date
def make_json_file(date, date_and_epoch_dic, filename):
    
    subreddits = ['wallstreetbets', 'stocks', 'CanadianInvestor']
    before_epoch = date_and_epoch_dic[date][0]
    after_epoch = date_and_epoch_dic[date][1]

    for reddit in subreddits:
        list_of_posts = []
        # We have divided up our calls into 5 parts of the day. Time stamps have been calculated using epoch
        # 84600/5 increments used  = 16920
        number_of_intervals = 5
        increment_time = 84600/number_of_intervals
        temp_before_epoch = before_epoch
        temp_after_epoch = after_epoch

        for i in range(0,number_of_intervals):
            print(i)
            data = requests.get(f'https://api.pushshift.io/reddit/search/submission/?subreddit={reddit}&after={temp_after_epoch}&before={temp_before_epoch}&size=100')
            x = json.loads(data.content.decode('utf8'))
            list_of_posts.append(x)
            temp_before_epoch = int(temp_before_epoch - increment_time)
            temp_after_epoch = int(temp_after_epoch + increment_time)

        write(list_of_posts, "output_file.json") 

        
       # break
    

def make_requests_to_reddit(date_and_epoch_dic):

    for date in date_and_epoch_dic:
        filename = date + '.json'
        if (does_cache_exist(filename) == False):
            make_json_file(date, date_and_epoch_dic, filename)
            break
            


# takes in a list of epoch, returns a dic with they key as the relevent date and before and after epochs to use
# date: [before, after] is the format of each entry
def format_epoch_based_on_date(list_of_epoch):
    date_and_epoch_dic = {}
    for i in range(0,6):
        if i == 0:
            continue
        else:
            current_date = epoch_to_date(list_of_epoch[i])
            #print("current date: ", current_date)
            date_and_epoch_dic[current_date] = [list_of_epoch[i-1], list_of_epoch[i]]
    return date_and_epoch_dic    

def find_intervals():

    time_between_days = 84600
    # returns epoch time in decimal, round to nearest int
    current_time =  int(round(time.time()))
    time_intervals = []
    start_current_day = current_time - (current_time % time_between_days)    
    date_time_stamps = []
    for i in range(8):
        date = datetime.utcfromtimestamp(start_current_day)
        if (date.weekday() < 5):
            print(date)
            time_intervals.append(start_current_day)
            start_current_day = start_current_day - time_between_days
        else:
            start_current_day = start_current_day - time_between_days
    print(time_intervals)
    print(current_time)

# function takes in file name based on date and checks to see if it is in cache
def does_cache_exist(filename):
    data_dir = 'data'
    cache_dir = 'cache'
    full_fname = osp.join(data_dir,cache_dir,filename)
    return os.path.exists(full_fname)

# takes time in epoch and returns relevent date
def epoch_to_date(epoch_time):
    time_in_datetime = time.strftime('%Y-%m-%d', time.localtime(epoch_time))
    #TODO: remove this later - %Y-%m-%d %H:%M:%S
    return time_in_datetime

def main():
    
    #list = [x1,x2,x3,x4,x5,x6]
    

    #print(does_cache_exist("30-Jan-2021.json"))
    
    list_of_epoch = [1611968400, 1611883800, 1611799200, 1611714600, 1611630000, 1611545400]
    date_dic = format_epoch_based_on_date(list_of_epoch)

    make_requests_to_reddit(date_dic)


 

    

if __name__ == '__main__':
    main()
