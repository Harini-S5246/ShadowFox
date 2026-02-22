num=145
char='o'
formatted_string=format(num,char)
print("Formatted String",formatted_string)
print()
radius=84
pi=3.14
area=pi*(radius**2)
print("Pond Area:",area,"square meters")
water_per_sqm=1.4
total_water=area*water_per_sqm
print("Total water:",int(total_water),"liters")
print()
distance=490
time_mins=7
time_secs=time_mins*60
speed=distance/time_secs
print("Speed: ",int(speed),"meters per second")