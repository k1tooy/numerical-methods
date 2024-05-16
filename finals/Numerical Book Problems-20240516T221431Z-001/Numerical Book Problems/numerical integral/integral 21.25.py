#21.25 A transportation engineering study requires that you determine the number of cars that pass through an intersection traveling
#during morning rush hour. You stand at the side of the road and
#count the number of cars that pass every 4 minutes at several times
#as tabulated below. Use the best numerical method to determine (a)
#the total number of cars that pass between 7:30 and 9:15, and (b)
#the rate of cars going

import numpy as np

# Given data
time = np.array([0, 15, 30, 45, 60, 75, 105])  # time in minutes from 7:30
rate = np.array([18, 24, 14, 24, 21, 9])  # rate in cars per 4 minutes

# Convert rate to cars per minute
rate_per_minute = rate / 4

# Apply the Trapezoidal rule to find the total number of cars
total_cars = 0
for i in range(len(time) - 1):
    total_cars += (time[i+1] - time[i]) * (rate_per_minute[i] + rate_per_minute[i+1]) / 2

# Calculate the average rate of cars per minute
total_time = time[-1] - time[0]
average_rate_per_minute = total_cars / total_time

print(f'(a) The total number of cars that pass between 7:30 and 9:15 is {total_cars:.2f}')
print(f'(b) The rate of cars going through the intersection per minute is {average_rate_per_minute:.2f} cars per minute')