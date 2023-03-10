# 1
# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, 
# from the number (as the 0th element) down to 0 (as the last element).
#       Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(number): # declaring the function 
    new_list = []
    for num in range(number, -1, -1): #starting at the highest range and counting down
        new_list.append(num)
    print(new_list) # printing each reverse countdown
    return new_list # ensuring to 
countdown(10)

# 2
# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def receive(number1, number2):
    print(number1)
    return number2
receive(10, 20)

#3
# First Plus Length - Create a function that accepts a list and returns the sum of the first value in 
# the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(a_list):
    sum = a_list[0] + len(a_list)
    return sum 
print(first_plus_length([1,2,3,4,5]))

#4
# Values Greater than Second - Write a function that accepts a list and creates a new list containing 
# only the values from the original list that are greater than its 2nd value. Print how many values this 
# is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def greater_than_second(a_second_list):
    new_list = []
    if len(a_second_list) < 2:
        return False 
    else:
        for index in range(len(a_second_list)):
            if a_second_list[index] > a_second_list[1]:
                new_list.append(a_second_list[index])
        return new_list

print(greater_than_second([5,2,3,2,1,4,3,5,7]))
print(greater_than_second([3]))

#5
# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The 
# function should create and return a list whose length is equal to the given size, and whose values are all 
# the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def this_length_that_value(size, value):
    str_value = str(value)
    output = list(str_value * size)

    new_output = []
    for x in output:
        new_output.append(int(x))
    
    return new_output
print(this_length_that_value(4,7))
