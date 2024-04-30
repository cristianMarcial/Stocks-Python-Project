This project's main purpose is to select from a list of provided stocks based on the amount to invest and the specified 
timeframe for the rate of return for the stock.

The Usecase is very simple: A person has X amount of money to invest in a stock and he/she wants to maximize his/her 
investment based on stock historical data for a specific timeframe.  Maybe the person wants to maximize based on one 
month of historical projection or five months, a year, or 5 years.

So the input to the program are:

1) List of stocks to choose from.  These stocks contain the stock price, name, 1 month, 6 months, 1 year and 5 years 
historical returns for that stock.  The stock file is a Comma comma-separate file (CSV) that will be passed as command 
line to your program and has the following format:

name,price,1M,6M,1Y,5Y

GOOGL,134.98,5.18,28.72,33.87,76.46

MSFT,323.23,0.45,17.98,33.25,182.75

IBM,150.03,5.43,18.5,18.76,3.76

HPQ,27.22,-13.06,-4.91,2.85,2.85

ORCL,113.38,-2.68,29.58,66.63,122.21

META,300.65,3.75,48.73,105.88,84.75

TSLA,265.51,14.62,34.17,-14.15,1229.27

Since you want to have a diversified portfolio you can only pick 1 stock for each company.  But if you still have money after 
picking the best stock for your timeframe your program can pick a fraction of the next stock.  So a common program run will be 
something like:

python ./stockPicker.py stocks.csv 300 1m

This will instruct your program to use the stocks from the "stocks.csv" file, let the program know you only have $300 dollars to 
spend in stocks and that you want to base your stock choice on the one-month rate of return (which will make your program focus 
on the 1M rates).  The valid rates that your program can accept are: "1m", "6m", "1y" and "5y".  

The output of your program must be in the following format:

['TSLA', '0.26 GOOGL']

This means that with a $300 investment and using only a month rate of returns, the best option to spend the $300 is to buy 1 stock 
from TSLA and 0.26 stocks of GOOGL. This output could be obtained if "py main.py stocks.csv 300 1m" is typed on the terminal.