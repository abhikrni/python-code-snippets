import datetime
import pytz

date = datetime.date.today()
#print(date.isoweekday())  #Monday - 1


# Time deltas are differences between times. So it can add/sub datetime objects


bday = datetime.date(2020, 5, 14)
today = datetime.date.today()


diff = bday - today
#print(diff.total_seconds())


current_time = datetime.time(23, 23, 23, 23)
#print(current_time.hour)


dt = datetime.datetime(2019, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)


