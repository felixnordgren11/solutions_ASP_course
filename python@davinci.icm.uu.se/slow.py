import time
# taken from geeksforgeeks.org

sleep_time_s = 60 # sleep for a minute

# printing the start time
print("The time of code execution begin is : ", time.ctime())

# using sleep() to hault the code execution
time.sleep(sleep_time_s)

# printing the end time
print("The time of code execution end is : ", time.ctime())