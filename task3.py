"""This program determines the award a person competing in a triathlon will receive"""

#read in variables
swimming = 30.4
running = 30.9
cycling = 40.0

total_time = running+cycling+swimming
print(total_time)

if total_time <= 100.0:
    print(f"You qualified in {total_time} minutes, with Provincial Colours!")
elif total_time <= 105.0:
    print(f"You qualified in {total_time} minutes, with Provincial Half Colours!")
elif total_time <= 110.0:
    print(f"You qualified in {total_time} minutes, with Provincial Scroll!")
else:
    print(f"You qualified in {total_time} minutes, with no award :(")