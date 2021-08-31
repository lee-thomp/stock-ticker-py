# stock-ticker-py
A simple python3 script to print a rough week's worth of daily stock information to the terminal.
Made for myself to add to my `.bashrc`.
Requires `yfinance`, `sys`, `datetime` modules.
The script takes a single stock ticker as input, for example:
```
$ stock-ticker AAPL
```
Which will return:

![Example output](images/screenshot.png)

Makefile by default installs to the user's `.local/bin`, adjust to taste.
