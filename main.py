try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

html = open('input.html', 'r') 
parsed_html = BeautifulSoup(html, features='html.parser')

#print(parsed_html.get_text())

table_text = parsed_html.get_text()

table_text = table_text.split('\n')

print(len(table_text))
# Have the necessary segmented data

# Split up by days?

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

schedule = []
index = 0
day_indexes = []

# Get the indexes of days
for tt_line in table_text:
    if tt_line in days:
        day_indexes.append(index)
    index += 1

print(day_indexes)

# Get the lines between the indexes, assign to day.
# Days are constant anyway, so can be hardcoded

sched_per_day = {}

sched_per_day['Mon'] = [day_indexes[0], day_indexes[1]]
sched_per_day['Tue'] = [day_indexes[1], day_indexes[2]]
sched_per_day['Wed'] = [day_indexes[2], day_indexes[3]]
sched_per_day['Thu'] = [day_indexes[3], day_indexes[4]]
sched_per_day['Fri'] = [day_indexes[4], len(table_text)-1]

print(sched_per_day)
# There is the option of incorporating Saturday, potential for an endpoint

for day in sched_per_day:
    print(sched_per_day[day][1] - sched_per_day[day][0])

