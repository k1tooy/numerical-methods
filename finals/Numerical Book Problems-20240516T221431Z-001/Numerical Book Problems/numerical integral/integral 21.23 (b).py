#21.23 Determine the distance traveled for the following data:
#t, min 1 2 3.25 4.5 6 7 8 9 9.5 10
#v, m/s 5 6 5.5 7 8.5 8 6 7 7 5
#(b) the best combination of the trapezoidal and Simpson’s rules,

# Apply Trapezoidal rule for first interval
distance_comb = (t[1] - t[0]) * (v[0] + v[1]) / 2

# Apply Simpson's 1/3 rule for the next six intervals
for i in range(1, 7, 2):
    h = t[i+2] - t[i]
    distance_comb += h * (v[i] + 4*v[i+1] + v[i+2]) / 6

# Apply Trapezoidal rule for the last two intervals
distance_comb += (t[8] - t[7]) * (v[7] + v[8]) / 2
distance_comb += (t[9] - t[8]) * (v[8] + v[9]) / 2

print(f'(b) Distance traveled using the best combination of the trapezoidal and Simpson’s rules is {distance_comb:.2f} meters')
