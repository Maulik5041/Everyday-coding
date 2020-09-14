"""Parsing the log files

    Q1. Extract timestamp from logs and convert to datetime object
    Q2. Extract shutdown events and calculate timedelta between
          first and the last shutdown initiated events"""


import requests
import re
import dateutil.parser
from datetime import datetime


def get_url(url):
    """access the url and return its content"""
    get_logs = requests.get(url)
    return get_logs.text


def convert_to_datetime(logs):
    """extracting the date from logs and converting to datetime"""
    extract_datetime = logs.split()[1]
    match_dt_string = '%Y-%m-%dT%H:%M:%S'
    final_datetime = datetime.strptime(extract_datetime, match_dt_string)
    return final_datetime


def time_between_shutdowns(logs_list):
    """getting the shutdown times and calculating the first and last"""
    shutdown_times = []
    for log_line in logs_list:
        if log_line and 'Shutdown initiated' in log_line:
            shutdown_times.append(convert_to_datetime(log_line))

    return max(shutdown_times) - min(shutdown_times)


if __name__ == '__main__':
    logs_url = 'https://bites-data.s3.us-east-2.amazonaws.com/messages.log'
    logs_content = get_url(logs_url)
    time_difference = time_between_shutdowns(logs_content.split('\n'))

    # accessing each element and converting dates to datetime
    # for log_line in logs_content.split('\n'):
    #     if log_line:
    #         print(convert_to_datetime(log_line))


"""
A more Pythonic Approach for time_between_shutdowns()

shutdown_entries = [log_line for log_line in log_list if 'Shutdown initiated' in log_line]
shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
return max(shutdown_times) - min(shutdown_times)
"""
