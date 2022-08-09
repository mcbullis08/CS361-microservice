# author: Jeremy Bullis
# date: 7/20/2022
# class: CS361
# description: Microservice for Portfolio project

#              This is the UI portion of the Micro tides service. It will provide all
#              the context to the user and request the information needed for
#              processing.
#
#              It will write the supplied date(s) to the date_range.txt file.
#
#              Finally, it will read requested tide information from tide_info.txt
#              and display that information to the user.

import time
import json
from datetime import date

write_path = 'date_range.txt'
read_path = 'tide_info.txt'


def get_user_date(choice):
    # function to read in user date or date range

    if choice == '1':
        with open(write_path, 'w') as write:
            temp = date.today()
            current_date = temp.strftime('%m/%d/%y')
            write.write(current_date)
            write.close()
    elif choice == '2':
        with open(write_path, 'w') as write:
            print('Please enter the first date: (mm/dd/yyyy)')
            first = input()
            write.write(first + '\n')
            print('and the second: (mm/dd/yyyy)')
            second = input()
            write.write(second)
            write.close()


def display_tide_data(data):
    # function to display the tide date and write it to a text file

    output = []                                                         # create hold for data display

    for entry in data['predictions']:
        user_date, tide_time = entry['t'].split()                                 # split time and date for display
        if entry['type'] == 'H':                                        # high tides
            if any(user_date in sublist for sublist in output):
                output.append([tide_time, 'High: ', entry['v']+' ft'])
            else:
                output.append([user_date])                                   # add new row if date is different
                output.append([tide_time, 'High: ', entry['v'] + ' ft'])
        elif entry['type'] == 'L':                                      # low tides
            user_date, tide_time = entry['t'].split()
            if any(user_date in sublist for sublist in output):
                output.append([tide_time, 'Low:  ', entry['v'] + ' ft'])
            else:
                output.append([user_date])                                   # add new row if date is different
                output.append([tide_time, 'Low:  ', entry['v'] + ' ft'])

    for row in output:
        print(row)

    print()


def main():
    while True:

        print('Would you like the tide report for today? or are you looking for a range of dates?')
        print("Press 1 for today, 2 for a range, or type 'quit' to quit.")

        choice = input()

        if choice == 'quit':
            break
        else:
            get_user_date(choice)

        time.sleep(3)

        with open(read_path, 'r') as r:
            data = json.load(r)
            r.close()

        display_tide_data(data)


if __name__ == "__main__":
    main()
