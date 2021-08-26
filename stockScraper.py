"""
Small program using the Python BeautifulSoup package and the requests module in order to web scrape a website for stock price information, and export it 
into a CSV file for further data interpretation. 
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
import os

tickerList = ["GME", "AMC", "BB", "WISH", "CLNE"]

def stockData(ticker):
    stock = "https://finance.yahoo.com/quote/" + ticker.upper()
    request = requests.get(stock)
    soup = BeautifulSoup(request.text, 'lxml')

    currentPrice = soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
    spaceSplit = soup.find("div", {"D(ib) Mend(20px)"}).find_all('span')[1].text.find(" ")
    priceChange = soup.find("div", {"D(ib) Mend(20px)"}).find_all('span')[1].text[:spaceSplit]
    percentChange = soup.find("div", {"D(ib) Mend(20px)"}).find_all('span')[1].text[spaceSplit+2:-1]

    output = {
        "ticker": ticker.upper(),
        "date": time.strftime("%d/%m/%Y"),
        "currentPrice": float(currentPrice),
        "percentChange":percentChange,
        "priceChange": float(priceChange)
    }
    return output

def csvExport(dict):
    filename = "myStocks.csv"
    if os.path.isfile(filename):
        with open(filename, "a", newline='') as file:
            write = csv.DictWriter(file, dict)
            write.writerow(dict)
    else:
        with open(filename, "w", newline='') as file:
            write = csv.DictWriter(file, dict)
            write.writeheader()
            write.writerow(dict)
            
for i in tickerList:
    x = stockData(i)
    print(x)
    csvExport(x)
