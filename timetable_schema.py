class TimetableSchema:
    def __init__(self):
        print('Schema Initiated')
        times = ['0800', '0830', '0900', '0930', '1000', '1030', '1100', '1130', '1200', '1230', '1300', '1330', '1400', '1430', '1500', '1530', '1600', '1630', '1700', '1730']
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
        schedule = {}

    def add_day(self, day, day_string):
        # Input: str(day) and string containing day and cell contents, csv
        # Objective: Filter string
        # Each populated cell starts and ends with four blanks
        # Each unpopulated cell contains '\xa0'
        cells = []
        blank_counter = 0
        index_counter = 0
        data_entry_mode = False

        for entry in day_string:
            if entry != '':
                blank_counter = 0

            if entry == '\xa0':
                cells.append('blank')
                
            elif entry == '':
                blank_counter += 1
            
                if blank_counter == 5: 
                    data_entry_mode = True
                    blank_counter = 0

            elif entry != '' and data_entry_mode:
                cells.append(entry + day_string[index_counter + 1])
                data_entry_mode = False
            index_counter += 1

        print(cells)


