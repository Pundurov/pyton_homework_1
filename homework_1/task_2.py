user_time = int(input("Enter the time in seconds: ")) # общее время в секундах

sec_time = user_time % 60
user_time = user_time // 60 # общее время в минутах
min_time = user_time % 60
hour_time = user_time // 60 # общее время в часах

print (f'{hour_time:02}:{min_time:02}:{sec_time}')
