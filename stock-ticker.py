#!/usr/bin/env python3

# Required packages
from yfinance import Ticker
from sys import stdout, argv, exit
from datetime import date, timedelta


# Neater colour clear function
def clr_code():
    stdout.write("\033[m")


def main(symbol):

    # Create one week data frame of daily price information
    stock_frame = Ticker(symbol).history(period = '1d', 
                                        start = date.today() - timedelta(7), 
                                        end = date.today())

    # Reset colours, print heading information (may require tuning for neatness)
    clr_code()
    print("$", symbol, "\t\t Open\t    Close")

    # Iterate through available days in frame
    for day in range(stock_frame.shape[0]):

        # Grab open/close price
        stock_open = stock_frame['Open'].iloc[day]
        stock_close = stock_frame['Close'].iloc[day]

        # Calculate direction, colourise appropriately
        if stock_open < stock_close:
            # Black on Green
            # 0 - non bold, 38;5 - 256color on system bg, 2 - green, 7 - reverse fg/bg
            stdout.write("\033[0;38;5;2;7m")

        else:
            # White on Red
            # 0 - non bold, 48;5 - white on 256color bg, 52 - dark red bg
            stdout.write("\033[0;48;5;52m")

        # Print formatted date string, tab, open price, arrow, close price
        print(stock_frame.index[day].strftime("%Y-%m-%d"),
                "\t", "%.2f" % stock_open,
                " -> ", "%.2f" % stock_close)

        # Clear colour codes at end of each line
        clr_code()

if __name__ == "__main__":

    # Check that a ticker is given at the command line
    if len(argv) == 1:
        print("Please provide a stock ticker to inspect, e.g. SPY")
        exit(1)
    main(argv[1])
