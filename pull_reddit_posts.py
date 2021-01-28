import datetime
import time
import os
import os.path as osp

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
def epoch_to_data(epoch_time):
    time_in_datetime = time.strftime('%Y-%m-%d', time.localtime(epoch_time))
    #TODO: remove this later - %Y-%m-%d %H:%M:%S
    return time_in_datetime

def main():
    
    #list = [x1,x2,x3,x4,x5,x6]
    

    #print(does_cache_exist("30-Jan-2021.json"))
    find_intervals()



 

    

if __name__ == '__main__':
    main()