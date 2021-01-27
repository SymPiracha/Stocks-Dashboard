import argparse
import json
import requests



def main():
	request_data = requests.get('https://cloud.iexapis.com/stable/stock/XOM/quote?token=pk_495c80fadacc450e8d8912f83b9d4053')

	data = json.loads(request_data.content.decode('utf8'))
	print(data)



if __name__ == '__main__':
	main()
