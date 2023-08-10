import datetime as dt

today = dt.datetime.today().strftime("%b %d, %Y")
today = dt.datetime.today()
print(today)
tomorrow = today + dt.timedelta(days=1)
print(tomorrow)

abc = [(today + dt.timedelta(days=i)).strftime("%b %d, %Y") for i in range(3)]
print(abc)