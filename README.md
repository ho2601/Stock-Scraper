# beautifulSoup-Python
Web Scraping also goes by names such as Web data extraction, screen scraping or web harvesting. <br>
This is an automated process used to extract information/data from a website which can later to used for something else.

My program is a Python script which web scapes Yahoo Finance for data (such as percentage increase, price increase etc...) related to the stocks. I also export the information into a CSV format so that the data may be analysed in other ways.

********************************************************************************************************
<h2>Steps of my program:</h2>
<h3>Step 1:</h3>
I made a function to extract the information such as the current price, price change, percent change etc... from the Yahoo Finance (https://finance.yahoo.com/quote/) website with the use of the beautifulSoup library and stored the data into variables, some string manipulation was used in order to format my data correctly. The information is then stored in a dictionary for easy formatting.

<h3> Step 2 </h3>
I created another function to store my web scrapped information into a CSV file so that it may be used in programs such as Excel in order to analyse the data further. This involved using the csv and os Python libraries.

<h3> Step 3 </h3>
For the code to work, I had to loop through the list of tickers and pass the tickers onto the stockData function to retrieve the data. The dictionary containing all the data will be outputted on the terminal for us to view upon each loop iteration. The dictionary data is then passed onto the csvExport function in order to export it into a CSV format for further use.
