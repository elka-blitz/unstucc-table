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
