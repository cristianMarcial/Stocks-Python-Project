from sys import argv
from csv import reader

def output(input):
    # Dictionary that contains the names of the stocks in the document sorted by their profits-to-price ratio. 
    stocks = {}

    # Contains the names of the stocks and their price.
    priceCatalog = {} 

    # The stocks that were spent.
    boughtStocks = []

    # Amount of money to invest in stocks.
    money = float(argv[2])

    # The variables 'stocks' and 'priceCatalog' are assigned a value according to their purpose.
    for line in input:
        stocks[line[0]] = float(line[rateFocus]) / float(line[1])
        priceCatalog[line[0]] = float(line[1])
        stocks = {k: v for k, v in sorted(stocks.items(), key=lambda item: item[1], reverse=True)}
    
    # The money will be spent through the iteration until there is less than the price of the last stock purchased.
    for i in stocks:
        if priceCatalog[i] <= money:
            boughtStocks.append(i)
            money -= priceCatalog[i]
        else:
            boughtStocks.append(str(round(money/float(priceCatalog[i]), 2)) + " " + i)
            break
    print(boughtStocks)

if len(argv) > 1: 
    with open(argv[1]) as file:
        # First line on the csv document. It has the name of the stocks, their prices and their rates of return.
        firstLine = next(reader(file))

        # This make the program focus on an specific rate given as the third argument on the command line.
        rateFocus = firstLine.index(argv[3].upper())

        # Returns a list of the stocks that were spent.
        output(reader(file))
    file.close()

# prueba: py main.py stocks.csv 300 1m
# resultado esperado: ['TSLA', '0.26 GOOGL']