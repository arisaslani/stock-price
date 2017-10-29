import pandas as pd
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2013, 1, 1)
end = datetime.datetime(2015, 1, 1)

f = web.DataReader("AAPL", 'google', start, end)

print(f.ix['2013-01-02'])
