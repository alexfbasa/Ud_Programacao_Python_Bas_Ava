# Ud_Programacao_Python_Bas_Ava
```text
https://knlearning.udemy.com/course/100-days-of-code/
https://www.udemy.com/course/100-days-of-code/
```

## Useful sites:
- Play with functions:
```text
https://reeborg.ca/
```
- Phyton tutorials
```text
https://developers.google.com/edu/python/lists#for-and-in
https://pythontutor.com/
```
- Create logos
```text
http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
```

## Basic
Print
Prints a string into the console. 
```commandline
print("Hello World")
```
Input
Prints a string into the console,
and asks the user for a string input.
```commandline
input("What's your name")
```
Comments
Adding a # symbol in font of text
lets you make comments on a line of code.
The computer will ignore your comments.
#This is a comment
```commandline
print("This is code")
```
Variables
A variable give a name to a piece of data.
Like a box with a label, it tells you what's
inside the box.
```commandline
my_name = "Angela"
my_age = 12
```
The += Operator
This is a convenient way of saying: "take the previous value and add to it".
```commandline
my_age = 12
my_age += 4
#my_age is now 16
```
## Data Types
Integers
Integers are whole numbers. 
```commandline
my_number = 354
```
Floating Point Numbers
Floats are numbers with decimal places.
When you do a calculation that results in a fraction e.g. 4 ÷ 3 the result will always be
a floating point number.
```commandline
my_float = 3.14159
```
Strings
A string is just a string of characters.
It should be surrounded by double quotes.
```commandline
my_string = "Hello"
```
String Concatenation
You can add strings to string to create
a new string. This is called concatenation.
It results in a new string.
```commandline
"Hello" + "Angela"
#becomes "HelloAngela"
```
Escaping a String
Because the double quote is special, it denotes a string, if you want to use it in
a string, you need to escape it with a "\"
```commandline
speech = "She said: \"Hi\""
print(speech)
#prints: She said: "Hi"
```
F-Strings
You can insert a variable into a string using f-strings.
The syntax is simple, just insert the variable in-between a set of curly braces {}.
```commandline
days = 365
print(f"There are {days}
in a year")
```
F U N C T I O N S
Creating Functions
This is the basic syntax for a function in Python. It allows you to give a set of
instructions a name, so you can trigger it multiple times without having to re-write
or copy-paste it. The contents of the function must be indented to signal that it's inside.
```commandline
def my_function():
print("Hello")
name = input("Your name:")print("Hello")
```
Calling Functions
You activate the function by calling it.
This is simply done by writing the name of the function followed by a set of round brackets. This allows you to determine
when to trigger the function and how many times.
```commandline
my_function()
my_function()
#The function my_function
#will run twice.
```
Functions with Inputs
In addition to simple functions, you can give the function an input, this way, each time the function can do something different
depending on the input. It makes your function more useful and re-usable.
```commandline
def add(n1, n2):
print(n1 + n2)
add(2, 3)
```
Functions with Outputs
In addition to inputs, a function can also have an output. The output value is proceeded by the keyword "return".
This allows you to store the result from a function.
```commandline
def add(n1, n2):
return n1 + n2
result = add(2, 3)
```
Variable Scope
Variables created inside a function are destroyed once the function has executed.
The location (line of code) that you use a variable will determine its value.
Here n is 2 but inside my_function() n is 3.
So printing n inside and outside the function will determine its value.
```commandline
n = 2
def my_function():
n = 3
print(n)
print(n) #Prints 2
my_function() #Prints 3
```
Keyword Arguments
When calling a function, you can provide a keyword argument or simply just the value.
Using a keyword argument means that you don't have to follow any order when providing the inputs.
```commandline
def divide(n1, n2):
result = n1 / n2
```
#Option 1:
```commandline
divide(10, 5)
```
#Option 2:
```commandline
divide(n2=5, n1=10)
```
C O N D I T I O N A L S
If
This is the basic syntax to test if a condition is true. If so, the indented code will be executed, if not it will be skipped.
```commandline
n = 5
if n > 2:
print("Larger than 2")
```
Else
This is a way to specify some code that will be executed if a condition is false.
```commandline
age = 18
if age > 16:
print("Can drive")
else:
print("Don't drive")
```
Elif
In addition to the initial If statement condition, you can add extra conditions to test if the first condition is false.
Once an elif condition is true, the rest of the elif conditions are no longer checked and are skipped.
```commandline
weather = "sunny"
if weather == "rain":
print("bring umbrella")
elif weather == "sunny":
print("bring sunglasses")
elif weather == "snow":
print("bring gloves")
```
and
This expects both conditions either side of the and to be true.
```commandline
s = 58
if s < 60 and s > 50:
print("Your grade is C")
```
or
This expects either of the conditions either side of the or to be true. Basically, both conditions cannot be false.
```commandline
age = 12
if age < 16 or age > 200:
print("Can't drive")
```
not
This will flip the original result of the condition. e.g. if it was true then it's now false.
```commandline
if not 3 > 1:
print("something")
#Will not be printed.
```
comparison operators
These mathematical comparison operators allow you to refine your conditional checks.
```text
> Greater than
< Lesser than
>= Greater than or equal to
<= Lesser than or equal to
== Is equal to
!= Is not equal to
```
L O O P S
While Loop
This is a loop that will keep repeating itself until the while condition becomes false.
```commandline
n = 1
while n < 100:
n += 1
```
For Loop
For loops give you more control than while loops. You can loop through anything
that is iterable. e.g. a range, a list, a dictionary or tuple.
```commandline
all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
print(fruit)
```
