try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

from timetable_schema import TimetableSchema

html = open('input.html', 'r') 
parsed_html = BeautifulSoup(html, features='html.parser')

#print(parsed_html.get_text())

table_text = parsed_html.get_text()

table_text = table_text.split('\n')

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

# Get the lines between the indexes, assign to day.
# Days are constant anyway, so can be hardcoded

line_indexes_per_day = {}

line_indexes_per_day['Mon'] = [day_indexes[0], day_indexes[1]]
line_indexes_per_day['Tue'] = [day_indexes[1], day_indexes[2]]
line_indexes_per_day['Wed'] = [day_indexes[2], day_indexes[3]]
line_indexes_per_day['Thu'] = [day_indexes[3], day_indexes[4]]
line_indexes_per_day['Fri'] = [day_indexes[4], len(table_text)-1]

# There is the option of incorporating Saturday, potential for an endpoint

#for day in line_indexes_per_day:
    #    print(line_indexes_per_day[day][1] - line_indexes_per_day[day][0])


# Get contents between the line index ranges
line_contents_per_day = {}

# Use the indexes established for each day
for day in line_indexes_per_day:
    line_contents_per_day[day] = []
    nav = 0
    start = line_indexes_per_day[day][0]
    end = line_indexes_per_day[day][1]
    # Iterate through lines until end index reached
    nav = start
    while nav != end:
        nav += 1
        line_contents_per_day[day].append(table_text[nav])

schema_load = TimetableSchema()

for day in line_contents_per_day:
    time_segs = schema_load.add_day(day, line_contents_per_day[day])
    value_assigned_time_segs = schema_load.assign_times(day, time_segs)






