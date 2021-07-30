friends = ['Carlos', 'Alex', 'Peyton', 'Eli']
for friend in friends:
    print("Hi " + friend)
	
---------------------------------------------------------
---------------------------------------------------------

	
for i in range(10):
  print("Hello, World!")
 
---------------------------------------------------------
---------------------------------------------------------

  

print((((1+2)*3)/4)**5)


---------------------------------------------------------
---------------------------------------------------------


# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")

def month_days(month,days):
    print(month + " has " + str(days) + " days.")

month_days("June",30)
month_days("July",31)

---------------------------------------------------------
---------------------------------------------------------


def f1(x, y):
	z = x*y  # the area is base*height
	print("The area is " + str(z))

def rectangle_area(base,height):
	area = base * height # the area is base*height
	print("The area is " + str(area))

rectangle_area(5,6)


---------------------------------------------------------
---------------------------------------------------------

Question 1
Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. 
Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown


---------------------------------------------------------
---------------------------------------------------------

Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". 
For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". 
Fill in this function so that it returns the proper grade.

def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60 :
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail



---------------------------------------------------------
---------------------------------------------------------

Complete the body of the format_name function. This function receives the first_name and last_name parameters and then returns a properly formatted string.

Specifically:

If both the last_name and the first_name parameters are supplied, the function should return like so:

print(format_name("Ella", "Fitzgerald"))
Name: Fitzgerald, Ella

If only one name parameter is supplied (either the first name or the last name) , the function should return like so:

Name: Adele

or

Name: Einstein

Finally, if both names are blank, the function should return the empty string:


def format_name(first_name, last_name):
	# code goes here
	if (first_name > "" and last_name > ""):
		return ("Name: " + last_name + ", " + first_name)
	else:
		return ("Name: " + last_name + first_name)

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

---------------------------------------------------------
---------------------------------------------------------

The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). 
Fill in the blank to make this happen.

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word3) and len(word2) >= len(word1):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))






---------------------------------------------------------
---------------------------------------------------------

The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). 
Complete the body of the function so that it returns the right number. 
Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	if denominator == 0:
		return 0
	fraction = numerator / denominator
	return fraction - int(fraction)

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0


---------------------------------------------------------
---------------------------------------------------------


Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. 
A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


---------------------------------------------------------
---------------------------------------------------------

The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.

Note: Try running your function with the number 0 as the input, and see what you get!

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  if n == 0:
    return False
  else:
    while n % 2 == 0:
      n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
      return True
    return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False




---------------------------------------------------------
---------------------------------------------------------

Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. 
A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
  if n == 0:
    return 0
  sum = 0
  # Return the sum of all divisors of n, not including n
  x = 1
  while x <= n-1:
    if n % x == 0:
      sum = sum + x
    x += 1
  return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


---------------------------------------------------------
---------------------------------------------------------

The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. 
An additional requirement is that the result is not to exceed 25, which is done with the break statement. 
Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24




---------------------------------------------------------
---------------------------------------------------------

Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included). 
Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

n = 0
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
        x += 1
    return sum

print(sum_squares(10)) # Should be 285




---------------------------------------------------------
---------------------------------------------------------

In math, the factorial of a number is defined as the product of an integer and all the integers below it. 
For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return the right number.

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
        i += 1
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120


---------------------------------------------------------
---------------------------------------------------------

The validate_users function is used by the system to check if a list of users is valid or invalid. 
A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. 
When calling it like in this example, something is not right. Can you figure out what to fix?

def validate_users(users):
  for user in [users]:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users("purplecat")




---------------------------------------------------------
---------------------------------------------------------

Fill in the blanks to make the factorial function return the factorial of n. 
Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
Remember that the factorial of a number is defined as the product of an integer and all integers before it. 
For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n))


---------------------------------------------------------
---------------------------------------------------------

Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1,11):
  print(x**3)



---------------------------------------------------------
---------------------------------------------------------

Write a script that prints the multiples of 7 between 0 and 100. 
Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.

for i in range(0,100,7): 
    print(i)



---------------------------------------------------------
---------------------------------------------------------

The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts. 
Currently the code will keep executing the function even if it succeeds. 
Fill in the blank so the code stops trying after the operation succeeded.

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break #The solution of this questions, was to add this break, to assure the script exits when succeeded.
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)


---------------------------------------------------------
---------------------------------------------------------

The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. 
For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


---------------------------------------------------------
---------------------------------------------------------

Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. 
For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

def sum_positive_numbers(n):
  if n < 1:
    return 0
  return  n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15



---------------------------------------------------------
---------------------------------------------------------

The count_users function recursively counts the amount of users that belong to a group in the company system, 
by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members. 
But it has a bug! Can you spot the problem and fix it?

def count_users(group):
  count = 0
  for member in get_members(group):
    if is_group(member):
      count += count_users(member)
    else:
      count += 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18


---------------------------------------------------------
---------------------------------------------------------

Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. 
Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  elif number == base:
    return True
  # Recursive case: keep dividing number by base.
  return is_power_of(number / base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

---------------------------------------------------------
---------------------------------------------------------

Fill in the blanks of this code to print out the numbers 1 through 7.

number = 1
while number <= 7:
	print(number, end=" ")
	number += 1


---------------------------------------------------------
---------------------------------------------------------

The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.

def show_letters(word):
	for x in word:
		print(x)

show_letters("Hello")
# Should print one line per letter



---------------------------------------------------------
---------------------------------------------------------

Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. 
Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
	count = 0
	if n == 0:
		return 1
	while (n != 0):
		n //=10
		count += 1
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1



#Also is possible to do the same with:
def digits(n):
    if n == 0:
	    return 1
    else:
	    count = str(n)
	    return len(count)


---------------------------------------------------------
---------------------------------------------------------

This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). 
Fill in the blanks so that calling multiplication_table(1, 3) will print out:
1 2 3
2 4 6
3 6 9

def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()


multiplication_table(1, 3)
# Should print the multiplication table shown


---------------------------------------------------------
---------------------------------------------------------

The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. 
Fill in the blanks to make this work correctly.

def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			x -= 1
			if x >= stop:
				return_string += ","
		return return_string
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			x += 1
			if x <= stop:
				return_string += ","
		return return_string
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


---------------------------------------------------------
---------------------------------------------------------

The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. 
For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.

def even_numbers(maximum):
	return_string = ""
	if maximum < 2:
	    return return_string
	for x in range(1,maximum+1):
		z = x % 2
		if z == 0:
			return_string += str(x)
			if x <= maximum:
				return_string += " "
				
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed




---------------------------------------------------------
---------------------------------------------------------

How does this function need to be called to print yes, no, and maybe as possible options to vote for?

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

votes(['Yes', 'No', 'Maybe'])


---------------------------------------------------------
---------------------------------------------------------

Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. 
For example, double_word("hello") should return hellohello10.

def double_word(word):
    word_doubled = word * 2
    return word_doubled + str(len(word_doubled))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

---------------------------------------------------------
---------------------------------------------------------

Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, 
False if they’re different. Remember that you can access characters using message[0] or message[-1]. 
Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))



---------------------------------------------------------
---------------------------------------------------------

Try using the index method yourself now!

Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".

word = "supercalifragilisticexpialidocious"
print(word.index("x"))



---------------------------------------------------------
---------------------------------------------------------

def replace_domain(email, old_domain, new_domain):
	if "@" + old_domain in email:
		index = email.index("@" + old_domain)
		new_email = email[:index] + "@" + new_domain
		return new_email
	return email	




---------------------------------------------------------
---------------------------------------------------------

Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. 
For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS



---------------------------------------------------------
---------------------------------------------------------

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

#It will print
#Hello Manny, your lucky number is 15

#You can also use format method in this other way

name = "Manny"
#number = 0
print("Hello your lucky number is {number}, {name}.".format(name = name, number= len(name) * 3))

---------------------------------------------------------
---------------------------------------------------------

Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". 
For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

---------------------------------------------------------
---------------------------------------------------------

#Format decimal numbers
price = 7.5
with_tax = price * 1.09
print (price, with_tax)

#it will print
# 7.5 8.175

#To format the result to display only 2 decimals
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

---------------------------------------------------------
---------------------------------------------------------

def to_celsius(x):
	return (x-32)*5/9
for x in range(0,101,10):
	print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))


---------------------------------------------------------
---------------------------------------------------------

The is_palindrome function checks if a string is a palindrome. 
A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. 
Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". 
Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for x in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if x != " ":
			new_string += x.lower()
		#	reverse_string = ___
	reverse_string = ''.join(reversed(new_string))
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


---------------------------------------------------------
---------------------------------------------------------

Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. 
For example, convert_distance(12) should return "12 miles equals 19.2 km".

def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

---------------------------------------------------------
---------------------------------------------------------

If we have a string variable named Weather = "Rainfall", which of the following will print the substring or all characters before the "f"?

Weather = "Rainfall"
print(Weather[:4])



---------------------------------------------------------
---------------------------------------------------------

Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. 
For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 


---------------------------------------------------------
---------------------------------------------------------

The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. 
If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. 
For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. 
The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).

def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence.rindex(old)
		new_sentence = sentence[:i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"


---------------------------------------------------------
---------------------------------------------------------

x = ["Now", "we", "are", "cooking"]
type(x)
displays <class 'list>

print(x)
displays ["Now", "we", "are", "cooking!"]

len(x)
4

"are" in x
displays True

"Today in x
displays False

print(x[0])
displays Now

print(x[3])
displays cooking!

x[1:3]
displays ["we", "are"]

x[:2]
displays ['Now', 'we']

x[2:]
displays ['are', cooking!']

---------------------------------------------------------
---------------------------------------------------------

Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word 
from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word 
in this sentence. 
Hint: remember that list indexes start at 0, not 1.

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


---------------------------------------------------------
---------------------------------------------------------


---------------------------------------------------------
---------------------------------------------------------

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
displays ["Pineapple", "Banana", "Apple", "Melon", "Kiwi"]

fruits.insert(0, "Orange")
print(fruits)
displays ["Orange", "Pineapple", "Banana", "Apple", "Melon", "Kiwi"]

#if you use a larger number that the len(fruits) with insert() method
#it will add the new item to the end of the list
#To add item to the end of the list, is easier to use append() method

fruits.insert(25, "Peach")
print(fruits)
displays ["Orange", "Pineapple", "Banana", "Apple", "Melon", "Kiwi", "Peach"]

#If you want to remove an item from a list, use remove() method
fruits.remove("Melon")
print(fruits)
displays ["Orange", "Pineapple", "Banana", "Apple", "Kiwi", "Peach"]

#Other form to remove an item from a list is with pop() method
# pop() method returns the item and also remove ir from the list
fruits.pop(3)
displays Apple
print fruits
displays ["Orange", "Pineapple", "Banana", "Kiwi", "Peach"]

#To change an item in a list do it assigning a new item to the specific index
fruits[2] = "Strawberry"
print fruits
displays ["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"]
---------------------------------------------------------
---------------------------------------------------------

The skip_elements function returns a list containing every other element from an input list, starting with the first element. 
Complete this function to do that, using the for loop to iterate through the input list.

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0
	# Iterate through the list
	for i in range(len(elements)):
		# Does this element belong in the resulting list?
		if i == 0 or (i % 2) == 0:
			# Add this element to the resulting list
			new_list.append(elements[i])
		# Increment i
		#___

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

---------------------------------------------------------
---------------------------------------------------------
#TUPLES

def convert_seconds(seconds):
	hours = seconds // 3600
	minutes = (seconds - hours * 3600) // 60
	remaining_seconds = seconds - hours * 3600 - minutes * 60

result = convert_seconds(5000)
type(result)
displays <class 'tupple'>

print(result)
displays (1, 23, 20)

hours, minutes, seconds = result
print (hours, minutes, seconds)
displays 1 23 20

hours, minutes, seconds = convert_seconds(1000)
displays 0 16 40


---------------------------------------------------------
---------------------------------------------------------

Let's use tuples to store information about a file: its name, its type and its size in bytes. 
Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.

def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

---------------------------------------------------------
---------------------------------------------------------

Tuples

As we mentioned earlier, strings and lists are both examples of sequences. 
Strings are sequences of characters, and are immutable. Lists are sequences of elements of any data type, and are mutable. 
The third sequence type is the tuple. 
Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. 
They’re specified using parentheses instead of square brackets.

You might be wondering why tuples are a thing, given how similar they are to lists. 
Tuples can be useful when we need to ensure that an element is in a certain position and will not change. 
Since lists are mutable, the order of the elements can be changed on us. 
Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. 
A good example of this is when a function returns multiple values. 
In this case, what gets returned is a tuple, with the return values as elements in the tuple. 
The order of the returned values is important, and a tuple ensures that the order isn’t going to change. 
Storing the elements of a tuple in separate variables is called unpacking. 
This allows you to take multiple returned values from a function and store each value in its own variable.


---------------------------------------------------------
---------------------------------------------------------

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
	chars += len(animal)
	
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
displays Total characters: 22, Average length: 5.5



---------------------------------------------------------
---------------------------------------------------------

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
	print("{} - {}".format(index + 1, person)

displays
1 - Ashley
2 - Dylan
3 - Reese


---------------------------------------------------------
---------------------------------------------------------

Try out the enumerate function for yourself in this quick exercise. 
Complete the skip_elements function to return every other element from the list, 
this time using the enumerate function to check if an element is on an even position or an odd position.

def skip_elements(elements):
	# code goes here
	new_list = []
	for index, element in enumerate(elements):
		if index == 0 or (index % 2) == 0:
			new_list.append(elements[index])
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


---------------------------------------------------------
---------------------------------------------------------

def full_emails(people):
	result = []
	for email, name in people:
		result.append("{} <{}>".format(name, email)
	return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

displays ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']



---------------------------------------------------------
---------------------------------------------------------
#LIST COMPREHENSION

multiples = []
for x in range(1,11):
	multiples.append(x*7)

print(multiples)

#With list comprehesion you ca do the same with one single line of code
multiples_lc = [x*7 for x in range(1,11)]
print(multiples_lc)

#List comprehesion let us create new lists based on sequences or ranges

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lenghts = [len(language) for language in languages]
print(lenghts)

displays [6, 4, 4, 2, 4, 1]

#print all of the numbers divisible by 3 from 0 to 100
divisible_by_three = [x for x in range(0,101) if x % 3 ==0]
print(divisible_by_three)


---------------------------------------------------------
---------------------------------------------------------

The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. 
Hint: remember that list and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
	return [x for x in range(0,n+1) if x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


---------------------------------------------------------
---------------------------------------------------------

Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 
Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for filename in filenames:
    if filename.endswith('c'):
        newfilenames.append(filename)
    elif filename.endswith('t'):
        newfilenames.append(filename)
    else:
        index = filename.rindex('.hpp')
        newfilenames.append(filename[:index] + ".h")

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hp


---------------------------------------------------------
---------------------------------------------------------

# Let's create a function that turns text into pig latin: 
# a simple text transformation that modifies each word moving the first character to the end 
# and appending "ay" to the end. For example, python ends up as ythonpay.

def pig_latin(text):
  say = ""
  pig_latin_string = ""
  # Separate the text into words
  words = text.split()
  print(words)
  for word in words:
    # Create the pig latin word and add it to the list
    say += word[1:]+word[0]+"ay "
    # Turn the list back into a phrase
  return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


---------------------------------------------------------
---------------------------------------------------------

# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. 
# Each of the three values can be expressed as an octal number summing each permission, 
# with 4 corresponding to read, 2 to write, and 1 to execute. 
# Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
# For example: 
# 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----" 
# 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x" 
# Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for index in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if index >= value:
                result += letter
                index -= value
            else:
                result += '-'
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


---------------------------------------------------------
---------------------------------------------------------

# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … 
# For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

def group_list(group, users):
  members = ("{}: {}".format(group, ', '.join(users)))
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"




---------------------------------------------------------
---------------------------------------------------------

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence 
# "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) 
# should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. 
# Fill in the gaps in this function to do that.

def guest_list(guests):
	for x in guests:
		name, age, profession = x
		print("{} is {} years old and works as {}".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

---------------------------------------------------------
---------------------------------------------------------
# ---- DICTIONARIES ----

x = {}
type(x)
displays <class dict>

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
displays {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}

file_counts["txt"]
displays 14

print("jpg" in  file_counts)
displays True

print("html" in file_counts)
displays False

file_counts["cfg"] = 8
print(file_counts)
displays {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}

file_counts["csv"] = 17
print(file_counts)
displays {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}

del file_counts["cfg"]
print(file_counts)
displays {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23}

---------------------------------------------------------
---------------------------------------------------------

The "toc" dictionary represents the table of contents for a book. 
Fill in the blanks to do the following: 
1) Add an entry for Epilogue on page 39. 2) Change the page number for Chapter 3 to 24. 
3) Display the new dictionary contents. 4) Display True if there is Chapter 5, False if there isn't.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"]=39 # Epilogue starts on page 39
toc["Chapter 3"]=24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print('Chapter 5' in toc) # Is there a Chapter 5?



---------------------------------------------------------
---------------------------------------------------------

# Iterating over the content of a dictionary

file_counts = {"jpg":10, "txt":14, "csv": 2, "py":23}
for extension in file_counts
print(extension)
displays
jpg
txt
csv
py

---------------------------------------------------------
---------------------------------------------------------

file_counts = {"jpg":10, "txt":14, "csv": 2, "py":23}
for ext, amount in file_counts.items():
	print("There are {} files .{} extension".format(amount, ext))
displays
There are 10 files with the .jpg extension
There are 14 files with the .txt extension
There are 2 files with the .csv extension
There are 23 files with the .py extension

---------------------------------------------------------
---------------------------------------------------------

file_counts = {"jpg":10, "txt":14, "csv": 2, "py":23}

file_counts.keys()
displays dict_keys(['jpg', 'txt', 'csv', 'py'])

file_counts.values()
displays dict_values([10, 14, 2, 23])

for value in file_counts.values()
	print(value)
displays
10
14
2
23	

---------------------------------------------------------
---------------------------------------------------------

Now, it's your turn! Have a go at iterating over a dictionary!

Complete the code to iterate through the keys and values of the cool_beasts dictionary. 
Remember that the items method returns a tuple of key, value for each element in the dictionary.

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, part in cool_beasts.items():
    print("{} have {}".format(beast, part))

Here is your output:
octopuses have tentacles
dolphins have fins
rhinos have horns

---------------------------------------------------------
---------------------------------------------------------

def count_letters(text):
	result = {}
	for letter in text:
		if letter not in result:
			result[letter] = 0
		result[letter] +=1
	return result
	
print(count_letters("aaaaa"))
displays {'a': 5}
print(count_letters("tenant"))
displays {'t': 2, 'e': 1, 'n': 2, 'a': 1}
print(count_letters("a long string with a lot of letters"))
displays {'i': 2, 'l': 3, 'f': 1, 'h': 1, 't': 5, 'e': 2, 'r': 2, 'n': 2, 'g': 2, 'w': 1, 'a': 2, ' ': 7, 'o': 3, 's': 2}


---------------------------------------------------------
---------------------------------------------------------

#DICTIONARIES VS. LISTS

# Example for a list
ip_addresses = [ '192.168.1.1', '127.0.0.1', '8.8.8.8']

# Example for a dictionary
host_addresses = {'router': '192.168.1.1', 'localhost': '127.0.0.1', 'google': '8.8.8.8'}

#You want to use dictionaries when you plan on searching a specific element.



---------------------------------------------------------
---------------------------------------------------------

In Python, a dictionary can only hold a single value for a given key. 
To workaround this, our single value can be a list containing multiple values. 
Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, color in wardrobe.items():
	for x in range(len(color)):
		print("{} {}".format(color[x], item))

Here is your output:
red shirt
blue shirt
white shirt
blue jeans
black jeans



---------------------------------------------------------
---------------------------------------------------------
# Practice Quiz Dictionaries

The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
    emails = []
    for email, users in domains.items():
        for user in users:
            emails.append("{}@{}".format (user, email))
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

displays	['clark.kent@gmail.com', 'diana.prince@gmail.com', 'peter.parker@gmail.com', 'barbara.gordon@yahoo.com', 'jean.grey@yahoo.com', 'bruce.wayne@hotmail.com']

---------------------------------------------------------
---------------------------------------------------------

The groups_per_user function receives a dictionary, which contains group names with the list of users. 
Users can belong to multiple groups. 
Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user in user_groups:
				user_groups[user].append(group)
			else:
				user_groups[user] = [group]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
		
displays	{'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}


---------------------------------------------------------
---------------------------------------------------------

The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries are replaced and new entries are added. 
What is the content of the dictionary “wardrobe“ at the end of the following code?

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

print(wardrobe)
displays	{'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}



---------------------------------------------------------
---------------------------------------------------------
What’s a major advantage of using dictionaries over lists?

* It's quicker and easier to find a specific element in a dictionary


---------------------------------------------------------
---------------------------------------------------------
The add_prices function returns the total price of all of the groceries in the dictionary. 
Fill in the blanks to complete this function.

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for price in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price

	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44



---------------------------------------------------------
---------------------------------------------------------
QUIZ WEEK 4 :: DICTIONARIES
---------------------------------------------------------
---------------------------------------------------------
1
The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". 
The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. 
For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
  # Declare variables
  house_number =""
  street_name = ""
  address_list = address_string.split()
  # Separate the address string into parts

  # Traverse through the address parts
  for i in range(len(address_list)):
    if i == 0:
      house_number = address_list[i]
    else:
      street_name += address_list[i] + " "
  if street_name.endswith(" "):
    street_name = street_name[:-1] # remove las space char
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"




---------------------------------------------------------
---------------------------------------------------------
2
The highlight_word function changes the given word in a sentence to its upper-case version. 
For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
Can you write this function in just one line?

def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


---------------------------------------------------------
---------------------------------------------------------
3
A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. 
Drew was the first one to note which students arrived, and then Jamie took over. 
After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. 
Jamie emailed a follow-up, saying that her list is in reverse order. 
Complete the steps to combine them into one list as follows: 
the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
# Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  main_list = list2
  for guest in reversed(list1):
    main_list.insert(len(main_list), guest)
  return main_list
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

displays	['Mike', 'Carol', 'Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Alice']


---------------------------------------------------------
---------------------------------------------------------
4
Use a list comprehension to create a list of squared numbers (n*n). 
The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively. 
For example, squares(2, 3) should return [4, 9].

def squares(start, end):
	return [x**2 for x in range(start,end+1) ]


print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

---------------------------------------------------------
---------------------------------------------------------
5
Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

def car_listing(car_prices):
  result = ""
  for car, price in car_prices.items():
    result += "{} costs {} dollars".format(car, price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

displays	Kia Soul costs 19000 dollars
			Lamborghini Diablo costs 55000 dollars
			Ford Fiesta costs 13000 dollars
			Toyota Prius costs 24000 dollars

---------------------------------------------------------
---------------------------------------------------------
6
Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, 
with names of their friends and how many guests each friend is bringing. 
Each dictionary is a partial list, but Rory's list has more current information about the number of guests. 
Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, 
if a name is included in both dictionaries. Then print the resulting dictionary.

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  new_dict = guests2.copy()   # start with x's keys and values
  new_dict.update(guests1)    # modifies z with y's keys and values & returns None
  return new_dict
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

displays	{'David': 1, 'Nancy': 1, 'Robert': 4, 'Adam': 2, 'Samantha': 3, 'Chris': 5, 'Brenda': 3, 'Jose': 3, 'Charlotte': 2, 'Terry': 1}


---------------------------------------------------------
---------------------------------------------------------
7
Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. 
Upper case should be considered the same as lower case. 
For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
  result = {}
  text = text.lower()
  characters = '''! +=()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''
  for character in characters:
    text = text.replace(character, "")
  # Go through each letter in the text
  for letter1 in text:
    counter = 0
    # Check if the letter needs to be counted or not
    for letter2 in text:
      if letter2 == letter1:
        counter += 1
      result.update({letter1: counter})
    # Add or increment the value in the dictionary
    ___
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}



---------------------------------------------------------
---------------------------------------------------------
8
What do the following commands return when animal = "Hippopotamus"?

>>> print(animal[3:6])
>>> print(animal[-5])
>>> print(animal[10:])

displays	pop
			t
			us



---------------------------------------------------------
---------------------------------------------------------
9
What does the list "colors" contain after these commands are executed?

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

displays	['red', 'white', 'yellow', 'blue']


---------------------------------------------------------
---------------------------------------------------------
10
What do the following commands return?

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()

displays	dict_keys(['router', 'localhost', 'google'])


---------------------------------------------------------
---------------------------------------------------------






---------------------------------------------------------
---------------------------------------------------------






---------------------------------------------------------
---------------------------------------------------------