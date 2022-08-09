# author: Jeremy Bullis
# date: 7/20/2022
# class: CS361
# description: Microservice for Portfolio project

#              This program will read a text file that contains today's date or a
#              date range in the format of MM/DD/YYYY.
#
#              It will then make an API call to a tide prediction service supplied
#              by NOAA.
#
#              Finally, the received data will be parsed for relevant data which
#              will be written out to a text file for use in another program


import requests
import time
import json

read_path = 'date_range.txt'
write_txt_path = 'tide_info.txt'


def get_user_date_range():
    # function to read a date range from a text file (format MM/DD/YYY)

    with open(read_path, 'r') as f:
        data = f.read().splitlines()
        f.close()

    return data


def get_tide_range(start, end):
    # API call for getting tide data for our location

    start_date = start
    end_date = end

    # to find a new station id visit https://tidesandcurrents.noaa.gov/map/index.html
    station_id = '8558690'  # INDIAN RIVER INLET, DE

    url1 = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=predictions&application=oregonstate_student' \
           '&begin_date=' + start_date + '&end_date=' + end_date + '&datum=MLLW&' \
            'station=' + station_id + '&units=english&time_zone=lst&interval=hilo&format=json'
    headers = {
        'accept': 'application / json'
    }

    r = requests.get(url1, headers=headers)
    station = r.json()

    return station


def get_todays_tides():
    # API call for getting tide data for our location for

    # to find a new station id visit https://tidesandcurrents.noaa.gov/map/index.html
    station_id = '8558690'  # INDIAN RIVER INLET, DE

    url1 = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=predictions&application=oregonstate_student' \
           '&date=today&datum=MLLW&' \
            'station=' + station_id + '&units=english&time_zone=lst&interval=hilo&format=json'
    headers = {
        'accept': 'application / json'
    }

    r = requests.get(url1, headers=headers)
    station = r.json()

    return station


def main():

    while True:

        time.sleep(1)

        dates = get_user_date_range()

        if len(dates) > 1:
            data = get_tide_range(dates[0], dates[1])
            with open(write_txt_path, 'w') as outfile:
                json.dump(data, outfile)
                outfile.close()
        else:
            data = get_todays_tides()
            with open(write_txt_path, 'w') as outfile:
                json.dump(data, outfile)
                outfile.close()


if __name__ == "__main__":
    main()
