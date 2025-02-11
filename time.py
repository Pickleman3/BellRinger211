from datetime import datetime 
c = datetime.now()
current_time = c.strftime('%H:%M:%S')
print('Current Time is:', current_time)
ehs_time = "22:18:00"
ehs_time_obj = datetime.strptime(ehs_time, '%H:%M:%S')
current_time_obj = datetime.strptime(current_time, '%H:%M:%S')
time_diff = ehs_time_obj - current_time_obj
print(time_diff)
