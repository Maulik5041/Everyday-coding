from datetime import datetime, timedelta


print('Press ENTER to start the focus period')
input()
start_time = datetime.now()
end_time = start_time + timedelta(seconds=30)

while datetime.now() < end_time:
    continue

print('Break time of 10 seconds starts')
break_start = datetime.now()
break_ends = break_start + timedelta(seconds=10)

while datetime.now() < break_ends:
    continue

print('Press ENTER to start the next focus period')
print('Press ctrl-c to end this pomodoro timer')
