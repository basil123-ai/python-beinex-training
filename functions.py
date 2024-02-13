
import math

# Function to calculate dactorial of given number
def calculate_factorial(fact_input) :
        if fact_input == 0:
            return 1
        else:
            return fact_input * calculate_factorial(fact_input - 1)

number = 5
print("Factorial is:", calculate_factorial(number))


# Function for binding string
def bind_age_and_name(name, age) :
    return "Hello,"+name+"! You are "+age+" years old."

print("string is:", bind_age_and_name('Basil', '23'))


# function to find max of three numbers
def find_max_of_three(numbers):
    if len(numbers) < 3:
        raise ValueError("List must contain at least three numbers.")
    
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

# Example usage
number_list = [10, 25, 15]
print("Maximum of the list is", find_max_of_three(number_list))


# reverse string
def reverse_string(input_string):
    return input_string[::-1]

# Example usage
print("Original string:", reverse_string('hello'))



# Write a Python function that accepts a string and counts the number of upper and lower case letters. 
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

# Example usage
input_string = "Hello, World!"
upper_count, lower_count = count_upper_lower(input_string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)


# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.  
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    
    # Iterate over odd numbers starting from 5 up to the square root of the number
    for i in range(5, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    
    return True

# Example usage
num = 23
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")



# Define a function that accepts 2 values and return its sum, subtraction and multiplication. Using 4 types of functions based on arguments and return type. 
def mathematic_opr_withoutparm() :
     a = int(input('Enter the number a:'))
     b = int(input('Enter the number b:'))
     c = a + b

     return c

print('the sum of and b is:', mathematic_opr_withoutparm())



def mathematic_opr_withparm(a, b) :
     c = a + b
     d = a - b
     return c, d

a = int(input('Enter the number a:'))
b = int(input('Enter the number b:'))

c, d = mathematic_opr_withparm(a, b)
print('the sum of and b is:',c , 'and subtracted result is:', d)




# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def sort_hyphen_separated_words(input_string):
    # Split the input string into a list of words
    words = input_string.split('-')
    # Sort the list of words alphabetically
    sorted_words = sorted(words)
    # Join the sorted words back into a hyphen-separated sequence
    sorted_sequence = '-'.join(sorted_words)
    
    return sorted_sequence

# Example usage
sample_items = "green-red-yellow-black-white"
result = sort_hyphen_separated_words(sample_items)
print("Sorted sequence:", result)



# Define a function that accepts roll number and returns whether the student is present or absent. 
def check_attendance(roll_number):
    # Assuming student attendance data is stored in a dictionary
    attendance_data = {
        101: "Present",
        102: "Absent",
        103: "Present",
        104: "Present",
        # Add more roll numbers and their attendance status as needed
    }
    
    # Check if the roll number exists in the attendance data
    if roll_number in attendance_data:
        return attendance_data[roll_number]
    else:
        return "Roll number not found"

# Example usage
roll_number = 101
attendance_status = check_attendance(roll_number)
print(f"Roll number {roll_number} is {attendance_status}")


# Define a function that accepts lowercase words and returns uppercase words. 
def convert_to_uppercase(word):
    return word.upper()

# Example usage
lowercase_words = "apple"
uppercase_words = convert_to_uppercase(lowercase_words)
print("Uppercase words:", uppercase_words)