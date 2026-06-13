# Enter total seconds and display the result in hours, minutes and seconds.
second_input = int(input("Enter the seconds: "))
second_result = second_input % 60 # sec
minute_result = second_input//60 % 60 #min
hour_result = second_input//3600 # hour
print(hour_result, ":",minute_result, ":", second_result)