print("Enter TB or GB for the advertised unit:")
unit = input('> ')

# Calculate the amount that the advertized capacity lies:
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print("Enter the advertized capacity:")
advertized_capacity = input('> ')
advertized_capacity = float(advertized_capacity)

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(advertized_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)