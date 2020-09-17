"""Design a stop watch

1. Track amount of time elapsed between presses
    enter key

2. With each key press starting a new 'lap'
3. Print lap number, total time and lap time
4. Thus do the following:

    Find current time and store it as timestamp
      and also start of each lap

    Keep a lap counter and increment every time
      user presses ENTER

    Calculate the elapsed time by subtracting

    Handle KeyboardInterrupt exception so the
      user can quit
"""


# Time module reads the systems clock
import time
from datetime import datetime, timedelta


def time_timer():
    input()  # press Enter to begin
    print('Stopwatch started...')
    print('Press ENTER to add another lap')
    start_time = time.time()  # get the first lap's start time
    end_time = start_time
    lap_num = 1

    # start tracking the lap times
    try:
        while True:
            input()
            lap_time = round(time.time() - end_time, 2)
            total_time = round(time.time() - start_time, 2)
            print(f'Lap #{lap_num}: {total_time} ({lap_time})', end='')
            lap_num += 1
            end_time = time.time()  # reset the last lap time

    except KeyboardInterrupt:
        # Handle the ctrl-c exception to keep its error message
        # from displaying
        print('\nDone.')


def datetime_timer():
    input()  # press Enter to begin
    print('Stopwatch started...')
    print('Press ENTER to add another lap')
    start_time = datetime.now()  # get the first lap's start time
    end_time = start_time
    lap_num = 1

    try:
        while True:
            input()
            lap_time = datetime.now() - end_time
            total_time = datetime.now() - start_time
            print(f'Lap #{lap_num}: \
{str(round(total_time.seconds + (total_time.microseconds / 1000000), 2))} \
({str(round(lap_time.seconds + (lap_time.microseconds / 1000000), 2))})', end='')
            lap_num += 1
            end_time = datetime.now()

    except KeyboardInterrupt:
        print('\nDone.')


def which_timer(attempts):
    # Display the program's instructions
    print('Press ENTER to begin')
    print('Afterwards, press ENTER to click the stopwatch')
    print('Press ctrl-c to quit')

    user_input = input('Press t for time timer and dt for datetime timer: ')

    if user_input == 't':
        print(f'\nUsing timer made from TIME module because\
 the user typed t')
        time_timer()

    elif user_input == 'dt':
        print(f'\nUsing timer made from DATETIME module because\
 the user typed dt')
        datetime_timer()

    else:
        attempts += 1

        print(f'\nYou entered {user_input} which is not a valid option.\
 Please select either t or dt ONLY.')

        if attempts < 4:
            print(f'\nWARNING: ONLY {4 - attempts} attempts remaining')
            which_timer(attempts)


if __name__ == '__main__':
    attempts = 1
    which_timer(attempts)
