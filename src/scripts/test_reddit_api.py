import argparse
import json
import requests
import time
import datetime


def main():

    time_between_days_in_epoch = 86400
    #current_time = time.mktime(datetime.datetime.now().timetuple())
    current_time = int(time.time())
    
    request_data = requests.get('https://api.pushshift.io/reddit/search/submission/?q=BB&subreddit=stocks&after=1611619200&before=1611705600&size=1')
    data = json.loads(request_data.content.decode('utf8'))
    #print(data['data'][0]['created_utc'])


    #mod_value = current_time%time_between_days_in_epoch

    print(current_time)


if __name__ == '__main__':
	main()
