from datetime import datetime, timedelta


def get_birthdays_per_week (users:list):
    all = {}
    today = datetime.today()
    for i in users: 
        if today.strftime('%A') == 'Monday': 
            today -= timedelta(days=2)
        if i['birthday'] < today or i['birthday'] > today + timedelta(weeks=1): 
            continue
        else:
            name = i['name']
            dayweek = i['birthday'].strftime('%A')
            if dayweek == 'Sunday' or dayweek == 'Saturday':
                dayweek = 'Monday'
            if dayweek not in all:
                all[dayweek] = [name]
            else:
                all[dayweek].append(name)
    
    for k, v in all.items():
        print(f'{k}: {", ".join(v)}')
    


if __name__ == '__main__':
    get_birthdays_per_week([
          {'name': 'Bill',
           'birthday': datetime(2023, 3, 16)},
          {'name': 'Atlas',
           'birthday': datetime(2023, 3, 18)},
          {'name': 'Luka',
           'birthday': datetime(2023, 3, 22)},
          {'name': 'Nola',
           'birthday': datetime(2023, 3, 22)},
          {'name': 'Floss',
           'birthday': datetime(2023, 3, 14)}])