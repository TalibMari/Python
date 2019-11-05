import datetime
now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime('%H:%M:%S on the %A, %B the %dth, %Y'))