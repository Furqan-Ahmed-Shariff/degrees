# write a program to calculate the execution time of a program
import time
import os

start_time = time.time()

os.system("python degrees.py large")

end_time = time.time()

execution_time = end_time - start_time

print("Execution time:", execution_time)
