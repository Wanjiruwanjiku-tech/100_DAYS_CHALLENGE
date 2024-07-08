# Create Variables

name = "Natalie Wanjiru Wanjiku";
age = 27;
# centimeters
height = 167.54;


# print variables
print('The varible name contains the value: {}'.format(name))
print('The varible age contains the value: {}'.format(age))
print('The varible height contains the value: {}'.format(height))

# print the type of the variables
# Use the type() function to get the data type of the variable

print('The data type of the variable name is: {}'.format(type(name)))
print('The data type of the variable age is: {}'.format(type(age)))
print('The data type of the variable height is: {}'.format(type(height)))

#  operators
#  1year == 365 days
# 1 month == 30 days
# 1year == 12 month

def years_to_months(age):
    return age * 12;

print('Your age in months is: ', years_to_months(27))

height_in_meters = height / 100;
print('Height in meters: {}'.format(height_in_meters))


num1 = 15;
num2 = 7;

# addition
print('\n\t Operations for {} and {}'.format(num1, num2))
print('Addition: ', num1 + num2)
print('Subtraction: ', num1 - num2)
print('Multiplication: ', num1 * num2)
print('Division: ', num1 / num2)
print('Modulus: ', num1 % num2)
print('Exponent: ', num1 ** num2)
print('Floor Division: ', num1 // num2)
