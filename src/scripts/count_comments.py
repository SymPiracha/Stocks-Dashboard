import json
import pandas as pd
import argparse

def reading_json(inputfile, title, name):

    if(name == "not found"):    #Checks if an unavailable stock was entererd so returns 0%
        return 0

    total_comment_count = 0
    count_for_name=0
    with open(inputfile) as f:        #loops through the json file line by line
        for line in f:
            data = json.loads(line)
            total_comment_count+= data['num_comments']+1      #adds the total number of comments for all the stocks
            if(title in data['title'] or name in data['title']):    #if the stock was the given stocl, then it notes its comments
                count_for_name+=data['num_comments']+1

    percentage_one = (count_for_name/total_comment_count)*100       #Calculates the percentage of the given stock for the day to 2 dp
    percentage = round(percentage_one,2)
    return percentage


def read_name_of_stock(title):
    #TODO: hardcoded files in stock_info.csv
    df = pd.read_csv('stock_info.csv')   #opens the stock directory file and converts it into dictionary
    d = df.to_dict()

    for column in range(len(d['Symbol'])):   ##Goes through the columns file, and find the given stock 
        if(d['Symbol'][column]== title):
            return (d['Name'][column])      ## if found, returns the full name associated to the stock

    notfound = "not found"              ##incase of an unkown file, returns a not found string

    return notfound




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = "Enter input file")
    parser.add_argument('stock_title', help = "name")

    args = parser.parse_args()

    input = args.input
    stock_title = args.stock_title
    x = reading_json(input, stock_title, read_name_of_stock(stock_title))

    print(str(x)+ "%")

if __name__ == '__main__':
    main()
