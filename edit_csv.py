import json
import requests
import csv

"""
Contains functions that manipulate csv in any given way
"""

#check if symbol already exists in csv
def symbol_exists_in_csv(stock_symbol):
    with open('stock_info.csv', "r") as f:
        csvreader = csv.reader(f, delimiter=",")
        for row in csvreader:
            if stock_symbol in row[0]:
                return True
    f.close()

    return False
        


#call the api in order to extract the name of company and returns it
def pull_data_for_stock(stock_symbol, api_token):

    if (symbol_exists_in_csv(stock_symbol) == False):
        #TODO: add try catch to ensure stock name entered is correct
        data = requests.get(f'https://cloud.iexapis.com/stable/stock/{stock_symbol}/quote?token={api_token}')
        data = json.loads(data.content.decode('utf8'))
        # data now is a python dictionary with a key of comapany name which can be used to get company name
        companyName = data['companyName']
        # return first word you get from companyName
        return companyName.split(" ")[0]
    else:
        return "Already Exists"
    

#function to add new Symbol to CSV
def add_to_csv(stock_symbol, api_token):
    companyName = pull_data_for_stock(stock_symbol, api_token)
    if (companyName != "Already Exists"):
        # data_to_add = [stock_symbol,companyName]
        # with open('stock_info.csv', 'a') as f_object:
        #     writer_object = csv.writer(f_object)
        #     writer_object.writerow(data_to_add)
        #     f_object.close()
        file = open('stock_info.csv','a')
        file.write("\n")
        file.write(",".join((stock_symbol,companyName)))
        file.close()


def main():
    api_token = 'pk_495c80fadacc450e8d8912f83b9d4053'
    add_to_csv('SNSS',api_token)


if __name__ == '__main__':
    main()