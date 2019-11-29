import datetime
import time

###########################################################################################################################################
def timestamp_to_date(my_timestamp):
    return datetime.datetime.fromtimestamp(my_timestamp)


###########################################################################################################################################
def date_to_timestamp(my_date):
    return time.mktime(datetime.datetime.strptime(my_date, "%Y%m%d%H%M%S").timetuple())


###########################################################################################################################################
def weekday_from_timestamp(my_timestamp):
    return datetime.datetime.fromtimestamp(my_timestamp).strftime('%a')


###########################################################################################################################################
def hour_from_timestamp(my_timestamp):
    return datetime.datetime.fromtimestamp(my_timestamp).strftime('%H')


###########################################################################################################################################
def day_timestamp_range_from_date(my_date):
    dt = datetime.datetime.strptime(my_date, '%Y%m%d%H%M%S')

    my_start = dt.replace(hour=0, minute=0, second=1).strftime('%Y%m%d%H%M%S')
    my_end = dt.replace(hour=23, minute=59, second=59).strftime('%Y%m%d%H%M%S')
    print("inside day_timestamp_range_from_date: ", my_start, my_end)
    day_range = [date_to_timestamp(my_start), date_to_timestamp(my_end)]

    return day_range


###########################################################################################################################################
def week_timestamp_range_from_date(my_date):
    dt = datetime.datetime.strptime(my_date, '%Y%m%d%H%M%S')

    start = dt - datetime.timedelta(days=dt.weekday())
    end = start + datetime.timedelta(days=6)

    my_start = start.replace(hour=0, minute=0, second=1).strftime('%Y%m%d%H%M%S')
    my_end = end.replace(hour=23, minute=59, second=59).strftime('%Y%m%d%H%M%S')
    print("inside week_timestamp_range_from_date: ", my_start, my_end)
    week_range = [date_to_timestamp(my_start), date_to_timestamp(my_end)]

    return week_range


###########################################################################################################################################
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)


###########################################################################################################################################
def month_timestamp_range_from_date(my_date):
    dt = datetime.datetime.strptime(my_date, '%Y%m%d%H%M%S')

    last_day = last_day_of_month(dt)
    my_start = dt.replace(day=1, hour=0, minute=0, second=1).strftime('%Y%m%d%H%M%S')
    my_end = dt.replace(day=int(last_day.strftime('%d')), hour=23, minute=59, second=59).strftime('%Y%m%d%H%M%S')
    print("inside week_timestamp_range_from_date: ", my_start, my_end)
    month_range = [date_to_timestamp(my_start), date_to_timestamp(my_end)]

    return month_range


###########################################################################################################################################