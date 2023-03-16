from datetime import datetime, timedelta


def get_birthdays_per_week (users:list):
    all = {}
    today = datetime.today()

    start_of_week = today - timedelta(days=today.weekday()) #Тиждень починається з понеділка
    end_of_week = start_of_week + timedelta(days=7) #Функція виводить користувачів з днями народження на тиждень вперед від поточного дня

    for i in users: 

        birthday = i['birthday']
        birthday = birthday.replace(year=today.year)
        
        if start_of_week <= birthday <= end_of_week: 
            name = i['name']
            dayweek = i['birthday'].strftime('%A')

            if dayweek == 'Sunday' or dayweek == 'Saturday': #Користувачів, у яких день народження був на вихідних, потрібно привітати у понеділок.
                dayweek = 'Monday'

            if dayweek not in all:
                all[dayweek] = [name]
            else:
                all[dayweek].append(name)
    
    for k, v in all.items():
        print(f'{k}: {", ".join(v)}')
    


if __name__ == '__main__':
    get_birthdays_per_week([ #Для відладки зручно створити тестовий список users та заповнити його самостійно.
          {'name': 'Bill',
           'birthday': datetime(1976, 3, 16)},
          {'name': 'Atlas',
           'birthday': datetime(1956, 3, 18)},
          {'name': 'Luka',
           'birthday': datetime(2004, 3, 22)},
          {'name': 'Nola',
           'birthday': datetime(2012, 3, 18)},
          {'name': 'Floss',
           'birthday': datetime(1945, 3, 14)}])