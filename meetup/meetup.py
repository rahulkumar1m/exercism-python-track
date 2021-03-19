import calendar

def meetup(year, month, week, day_of_week):
    dow = dict(zip(list(calendar.day_name), range(7)))
    cal = calendar.Calendar()

    # Get all days with correct month and weekday
    days = [d for d in cal.itermonthdates(year,month) if d.weekday() == dow[day_of_week] and d.month == month]

    if week == 'teenth':
        meetup = [d for d in days if d.day >= 13 and d.day <= 19][0]
    elif week == 'last':
        meetup = days[-1]
    else:
        try:
            meetup = days[int(week[0]) - 1]
        except:
            raise MeetupDayException("....")
    
    return meetup

class MeetupDayException(Exception):
    pass
