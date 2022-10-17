#import all necessary modules
import sys, datetime, calendar, os
from datetime import date
#Ascii intro 
f = open(r"C:\Users\jeevz\Desktop\Tasklist\Ascii\asciiintro.txt", 'r')
print(''.join([line for line in f]))
f.close()
f2 = open(r"C:\Users\jeevz\Desktop\Tasklist\Ascii\asciiintro2.txt","r")
print(''.join([line for line in f2]))
f2.close()
#finding the day and storing it in day_name variable so as to open the correct day file
current_date = date.today()
day_name = calendar.day_name[current_date.weekday()]
#day list 
day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# writing a couple of if statements to check and open the correct file for the correct day
print(f"Today is a great {day_name}")
print("This is a terminal based application!")
print("To create a new task type 'taskcreate' and follow the steps")
print("To delete tasks for an entire day type 'tasktrash'")
print("To see all the task logs type 'taskshow'")
print("To exit the app type 'exit'")
print("To know what day it is type 'nameday'")
#function to automate inputting tasks
def task_input(name_of_the_day):
    user_input_2 = ""
    while user_input_2 != "done":
        user_input_2 = input("TASK$$")
        stripped_ui_2 = user_input_2.strip()
        if stripped_ui_2 != "done":
            name_of_the_day.write(user_input_2+"\n")
#function for asthetic purposes
def separators():
    print("***************----------------------------***************")
#function that helps to show tasks which were scheduled earlier
def show_off(name_of_the_day_2):
    if name_of_the_day_2 in day_list:
        file_size = os.path.getsize(f"{name_of_the_day_2}.txt")
        if file_size == 0:
            print(f"You have no tasks scheduled for {name_of_the_day_2}")
        else:
            task_file_open = open(f"{name_of_the_day_2}.txt", "r")
            task_list = task_file_open.readlines()
            n = 0
            len_task_list = len(task_list)
            while n < len_task_list:
                print(task_list[n])
                n += 1
            task_file_open.close()
    else:
        print(f"{name_of_the_day_2} does not exist")
        pass 

#function used to trash tasks
def trashy(name_of_the_day_3):
    if name_of_the_day_3 in day_list:
        trashy_open_file = open(f"{name_of_the_day_3}.txt", "w")
        trashy_open_file.truncate(0)
        trashy_open_file.close()
        print(f"All tasks for {name_of_the_day_3} has been deleted")
    else:
        print(f"{name_of_the_day_3} does not exist")
    
#logic
run = True
while run:
    user_input = input(">>")
    stripped_ui = user_input.strip()
    if stripped_ui == "nameday":
        print(f"Today's a great {day_name}")
#could've made line 58-93 to 4 lines, just for fun :) 
    elif stripped_ui == 'taskcreate':
        if day_name == "Sunday":
            sunday = open("Sunday.txt", "r+")
            task_input(sunday)
            sunday.close()
            separators()
        if day_name == "Monday":
            monday = open("Monday.txt", "r+")
            task_input(monday)
            monday.close()
            separators()
        if day_name == "Tuesday":
            tuesday = open("Tuesday.txt", "r+")
            task_input(tuesday)
            tuesday.close()
            separators()
        if day_name == "Wednesday":
            wednesday = open("Wednesday.txt", "r+")
            task_input(wednesday)
            wednesday.close()
            separators()
        if day_name == "Thursday":
            thursday = open("Thursday.txt", "r+")
            task_input(thursday)
            thursday.close()
            separators()
        if day_name == "Friday":
            friday = open("Friday.txt", "r+")
            task_input(friday)
            friday.close()
            separators()
        if day_name == "Saturday":
            saturday = open("Saturday.txt", "r+")
            task_input(saturday)
            saturday.close()
            separators()
    elif stripped_ui == "taskshow":
        print("***Enter the name of the day you want to check logs for***")
        user_input_3 = ""
        while user_input_3 != "done":
            user_input_3 = input("SHOW$$")
            stripped_ui_3 = user_input_3.strip()
            if stripped_ui_3 != "done":
                titled_input = stripped_ui_3.title()
                show_off(titled_input)
    elif stripped_ui == "tasktrash":
        print("***Enter the name day you want to delete the trash for***")
        user_input_4 = ""
        while user_input_4 != "done":
            user_input_4 = input("TRASH$$")
            stripped_ui_4 = user_input_4.strip()
            if stripped_ui_4 != "done":
                titled_input_2 = stripped_ui_4.title()
                trashy(titled_input_2)
            
#exit           
    elif stripped_ui == "exit":
        exit()
#invalid command characters identification
    elif stripped_ui != "nameday":
        print("Invalid command")
    elif stripped_ui != "taskcreate":
        print("Invalid command")
    elif stripped_ui != "taskshow":
        print("Invalid command")
    elif stripped_ui != "tasktrash":
        print(f"{stripped_ui} IS AN INVALID COMMAND")
        

    
    
