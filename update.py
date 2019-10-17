from ics import Calendar
from urllib.request import urlopen
url1 = "https://calendar.google.com/calendar/ical/marcel%40intuitionmachines.com/public/basic.ics"
url2 = "https://calendar.google.com/calendar/ical/dreamflasher%40dreamflasher.de/public/basic.ics"
c1 = Calendar(urlopen(url1).read().decode())
c2 = Calendar(urlopen(url2).read().decode())

for e in c2.events:
    c1.events.add(e)

with open('calendar.ics', 'w') as f:
    f.writelines(c1)
