"""  Home Work
create a program for Good moring sir accoding to current time 
# with import 

import time

hours =time.strftime("%H:%M:%S")
print(hours)

hours = int(time.strftime("%H"))
print(hours)

if 5 <= hours < 12:
    print("Good morning, sir!")
elif 12 <= hours < 17:
    print("Good afternoon, sir!")
elif 17 <= hours < 21:
    print("Good evening, sir!")
else:
    print("Good night, sir!")


    """

# Without Any import libray basic program 

Time=int(input("Enter the current time : "))

if 5<= Time < 12:
    print("Good morning sir !")
elif 12<= Time < 17:
  print("Good Afternoon sir !")
elif 17 <= Time <21:
    print("Good Evening sir !")
else:
    print("Good night sir !")