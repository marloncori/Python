try:
    import pandas_datareader as web
except:
    print(" You have to install that library with this commnad: \n\t pip install pandas-datareader")
finally:
    import math
    from time import sleep
    
    def progressBar(progress, total):
        percent = 100 * (progress / float(total))
        bar = '█' * int(percent) + '-' * (100 - int(percent))
        # alt+219
        cl = "\033[1;33m"
        fn = "\033[1;0m"
        print(cl + f"\r|{bar}| {percent:.2f}%" + fn, end="\r")
        sleep(0.03)

    def compute():
        numbers = [x * 5 for x in range(2000, 3000)]
        result = []
        print(" Hurra! Now you have a progress bar!")
        progressBar(0, len(numbers))
        for i, x in enumerate(numbers):
            result.append(math.factorial(x))
            progressBar(i + 1, len(numbers))

    def start():
        tickers = ["AAPI", "FB", "TSLA", "NVDA", "GS", "WFC"]
        closing_prices = []
        progressBar(0, len(tickers))
        for index, ticker in enumerate(tickers):
            last_price = web.DataReader(ticker, "yahoo").iloc[-1][Close]
            closing_prices.append(last_price)
            progressBar(index + 1, len(tickers))
        
    
    compute()        