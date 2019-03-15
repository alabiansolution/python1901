import datetime, random

x = datetime.datetime.now()

day = x.strftime("%a")
year = x.year
month = x.month
print(month, day+", " + str(year))
# print(help)

y = random.randint
