import datetime
# date_time = datetime.datetime(2023,5,23, hour=19, minute=24, second=50, microsecond=135)
# print(f'object datetime - {date_time}')
# print(f'type - {type(date_time)}')
#
# print(f'method date() - {date_time.date()}\ntype - {type(date_time.date())}')
# print(f'method time() - {date_time.time()}\ntype - {type(date_time.time())}')
#
# date_1=datetime.date(2021,9,24)
# time_1=datetime.time(5,38,48)
# print(f'date - {date_1}')
# print(f'time - {time_1}')
#
# date_and_time=datetime.datetime.combine(date_1, time_1)
# print(f'date&time - {date_and_time}\ntype - {type(date_and_time)}')
#
# print(f'new year = {date_1.replace(2023)}')
# print(f'date itself - {date_1}')

# date_now = datetime.datetime.now()
# date_today = datetime.datetime.today()
# date_date = datetime.date.today()
#
# print(f'now   {date_now}')
# print(f'today {date_today}')
# print(f'date  {date_date}')
# print(f'time now {date_now.time()}')
#
# print(f'weekday - {date_now.weekday()}')        # 0-6
# print(f'weekiso - {date_now.isoweekday()}')     # 1-7

# %A    - full weekday name
# %B    - full month name
# %d    - day of month
# %H    - hour (24)
# %m    - number of month
# %M    - minutes
# %S    - seconds
# %x    - date
# %X    - time
# %Y    - year

# date_now = datetime.datetime.now()
# print(f'date time to str = {date_now.strftime("%d.%m.%Y %H:%M (%A %B)")}')
#
# date_str = '28/09/2023 11:20'
# date_str_res = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')
# print(f'str to datetime = {date_str_res}')

# date_now = datetime.datetime.now()
# date_how = datetime.datetime(2022,2,24)
# print(date_now - date_how)
#
# print(f'now {date_now}')
# delta=datetime.timedelta(days=20, hours=8,weeks=4)
# print(f'delta {delta}')
# print(date_now - delta)
# a = date_now - delta
# print(a.strftime("%d.%m.%Y %H:%M"))

# try :
#     while True :
#         action = input('enter action (today/weekday/time/until/after/end) - ')
#         if action == "today" :
#             date_now = datetime.datetime.now()
#             print(f'today is {date_now.strftime("%d.%m.%Y (%A)")}')
#         elif action == "time" :
#             date_now = datetime.datetime.now()
#             print(f'now is {date_now.strftime("%H:%M")}')
#         elif action == "weekday" :
#             t_day = input("enter the date (dd/mm/yyyy): ")
#             date_now = datetime.datetime.strptime(t_day, '%d/%m/%Y')
#             print(f'{t_day} is {date_now.strftime("%A")}')
#         elif action == "until" :
#             t_day = input("enter the date (dd/mm/yyyy): ")
#             date_how = datetime.datetime.strptime(t_day, '%d/%m/%Y')
#             date_now = datetime.datetime.now()
#             days = date_how-date_now
#             print(f'there are {days.days} days between {date_how.strftime("%d.%m.%Y")} and {date_now.strftime("%d.%m.%Y")}')
#         elif action == "after" :
#             t_day = int(input("enter number of days after today: "))
#             delta = datetime.timedelta(days=t_day)
#             date_now = datetime.date.today() + delta
#             print(f'{date_now.strftime("%d.%m.%Y")} is the date after {t_day} days from today')
#         elif action == 'end' :
#             break
#         else :
#             print(f'sorry, {action} is wrong choice')
#
# except :
#     print("sorry, wrong input")

import os

path='c:\windows\web'
path_1 = os.path.normpath("c:/windows/web")
path_2 = 'c:\\windows\\web'
path_3 = r'c:\windows\web'

# for path, dirnames, filenames in os.walk(path):
#     print(f'path - {path}')
#     print(f'dirs - {dirnames}')
#     print(f'file - {filenames}')

# root = 'C:\\'
# dir1 = input('enter folder 1 ')
# dir2 = input('enter folder 2 ')
# path = os.path.join(root, dir1, dir2)
# for path, dirnames, filenames in os.walk(path):
#     print(f'path - {path}')
#     print(f'dirs - {dirnames}')
#     print(f'file - {filenames}')

path = os.path.normpath('new_dir')
os.mkdir(path)
os.rmdir(path)


