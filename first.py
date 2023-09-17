#!/bin/python3

#STRING
#Print String
print("hello World!")
print('Hello World!')
print("""This string runs
multiple lines!""") #triple quote for multi-line
print("This string is "+"awesome!") #We can also concatenate
print('\n') #new line
print("Test that new line out.")

print('\n') #new line
#MATH
print(50 + 50) #add
print(50 - 50) #minus
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #total
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with remainder (or a float
print(50 // 6) #no remainder

print('\n') #new line
#VARIABLES AND METHODS

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

name = "Roul" #string
age = 28 #int
gpa = 3.5 #float - has a decimal 

print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round. NO

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n') #new line
#FUNCTIONS 

def who_am_i(): #this is a function without parameters
	name = "Roul" #local variable
	age = 28
	print("My name is " + name + " and I am " + str(age) + " years old.")
	
who_am_i()	

def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)	

def add(x,y):
	print(x + y)

add(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)

square_root(64)

def nl(): #newline
	print('\n')

nl()
#Boolean expression (True or False)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "Type"
print(type(bool5))

nl()
#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 5
less_than_qual_to = 7 <= 5

Test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False


nl()
#CONDITONAL STATEMENTS - if/else

def drink(money):
	if money >= 2:
		return "You've got yourself a drink"
	else:
		return "No drink for you"

print(drink(3))
print(drink(1))

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Comeback with more money"
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too young and too poor"		
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))	


nl()
#LISTS - Have brackets []
movies = ["Avatar", "The Matrix", "Mission Impossible"] #Index count as [0,1,2,3,4,5]

print(movies[2]) #return the third item in the list
print(movies[0]) #return the first item in the list
print(movies[0:2]) #return the the first and second index number but does not inclust last index number.
print(movies[1:])
print(movies[:1])
print(movies[-1]) #return last item in list

print(len(movies)) #count item in the list
movies.append("JAWS")
print(movies) #appends to the end of the list

movies.insert(2, "Hustle")
print(movies)

movies.pop() #remove the last item
print(movies)

movies.pop(0) #remove the first item
print(movies)

anis_movies = ['Horror', 'Thriller']
our_favorite_movies = movies + anis_movies
print(our_favorite_movies)

grades = [["Bob", 82], ["Alice, 90"], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)

nl()
#TUPLES - Do not change, ()
grades = ("a", "b", "c", "d", "e", "f")

print(grades[1])


nl()
#LOOPING

#For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	


#While loops = execute as long as True
i = 1

while i < 10:
	print(i)
	i += 1	 


nl()
#ADVANCED STRINGS

my_name = "Roul"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #This is a delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "               hello            "
print(too_much_space.strip())

print("A" in "Apple") #True
print("a" in "Apple") #False


letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("My favorite movies is {}.".format(movie))
print("My favorite movies is %s." % movies)
print(f"My favorite movies is {movies}.")


nl()
#DICTIONARIES - key/value pairs {}

drinks = {"Latte" : 7, "Espresso": 10, "Capucinno": 8} #drink is the key, price is the value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Frank"] #add a new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #add new key:value pair
print(employees)

drinks['Machiato'] = 8
print(drinks)

print(drinks.get("Machiato"))
