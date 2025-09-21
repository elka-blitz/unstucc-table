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
        day_elements = 0

        while day_elements != 20: # Timetable of length 20 (30min increments)
        # Trying while loop instead of for, to make a custom for loop?
            if index_counter > len(day_string) - 1:
                break

            entry = day_string[index_counter] 
            # day_string and index_counter need to be refactored
            # Variable names no longer reflective of what they contain 
            if entry == '\xa0':
                cells.append('blank')
                day_elements += 1

            elif entry == '':
                blank_counter += 1
            
            else:
                # What about scanning ahead until three non escape/blanks are gathered
                    # Correction, there's actually 5 details per event
                # Keep running total, move pointer by this amount after
                # Work logic for double detection later

                # Else covers all nonescape
                # Adjust counters accordingly? 
                # According to what? Maybe ''s >_>
                class_detail = [] # Stores classcell details, of which there are 5 possible
                detail_count = 1 
                secondary_index_pointer = index_counter
                class_detail.append(entry)
                
                while detail_count != 5: # Could also use a len() here
                    try:
                        secondary_index_pointer += 1
                        if day_string[secondary_index_pointer] != '' and day_string[secondary_index_pointer != '\xa0']:
                            detail_count += 1
                            class_detail.append(day_string[secondary_index_pointer])
                    
                    except IndexError:
                        break

                # Three details found, title, room, wks
                # Add number skipped to original pointer
                # Also add the class detail chunk to the overall cell register
                index_counter = (index_counter + (secondary_index_pointer - index_counter))
                cells.append(class_detail)
                

            index_counter += 1


        print(cells)


