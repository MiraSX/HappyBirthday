from datetime import datetime


def get_birthdays_per_week (users:list):
    all = {}
    for i in users:
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
           'birthday': datetime(2023, 3, 12)},
          {'name': 'Atlas',
           'birthday': datetime(2023, 3, 14)},
          {'name': 'Luka',
           'birthday': datetime(2023, 3, 10)},
          {'name': 'Nola',
           'birthday': datetime(2023, 3, 11)},
          {'name': 'Floss',
           'birthday': datetime(2023, 3, 14)}])