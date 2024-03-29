# Ud_Programacao_Python_Bas_Ava
Good tools
https://jsonviewer.stack.hu/

```text
https://knlearning.udemy.com/course/100-days-of-code/
https://www.udemy.com/course/100-days-of-code/
```
## PhytonTutor.com 
```
## Useful sites:
- Play with functions:
```text
https://reeborg.ca/

Host, run and Code python in the Cloud!
https://www.pythonanywhere.com/

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
```text
print("Hello World")
```
Input
Prints a string into the console,
and asks the user for a string input.
```text
input("What's your name")
```
Comments
Adding a # symbol in font of text
lets you make comments on a line of code.
The computer will ignore your comments.
#This is a comment
```text
print("This is code")
```
Variables
A variable give a name to a piece of data.
Like a box with a label, it tells you what's
inside the box.
```text
my_name = "Angela"
my_age = 12
```
The += Operator
This is a convenient way of saying: "take the previous value and add to it".
```text
my_age = 12
my_age += 4
#my_age is now 16
```
## Data Types
Integers
Integers are whole numbers. 
```text
my_number = 354
```
Floating Point Numbers
Floats are numbers with decimal places.
When you do a calculation that results in a fraction e.g. 4 ÷ 3 the result will always be
a floating point number.
```text
my_float = 3.14159
```
Strings
A string is just a string of characters.
It should be surrounded by double quotes.
```text
my_string = "Hello"
```
String Concatenation
You can add strings to string to create
a new string. This is called concatenation.
It results in a new string.
```text
"Hello" + "Angela"
#becomes "HelloAngela"
```
Escaping a String
Because the double quote is special, it denotes a string, if you want to use it in
a string, you need to escape it with a "\"
```text
speech = "She said: \"Hi\""
print(speech)
#prints: She said: "Hi"
```
F-Strings
You can insert a variable into a string using f-strings.
The syntax is simple, just insert the variable in-between a set of curly braces {}.
```text
days = 365
print(f"There are {days}
in a year")
```
F U N C T I O N S
Creating Functions
This is the basic syntax for a function in Python. It allows you to give a set of
instructions a name, so you can trigger it multiple times without having to re-write
or copy-paste it. The contents of the function must be indented to signal that it's inside.
```text
def my_function():
print("Hello")
name = input("Your name:")print("Hello")
```
Calling Functions
You activate the function by calling it.
This is simply done by writing the name of the function followed by a set of round brackets. This allows you to determine
when to trigger the function and how many times.
```text
my_function()
my_function()
#The function my_function
#will run twice.
```
Functions with Inputs
In addition to simple functions, you can give the function an input, this way, each time the function can do something different
depending on the input. It makes your function more useful and re-usable.
```text
def add(n1, n2):
print(n1 + n2)
add(2, 3)
```
Functions with Outputs
In addition to inputs, a function can also have an output. The output value is proceeded by the keyword "return".
This allows you to store the result from a function.
```text
def add(n1, n2):
return n1 + n2
result = add(2, 3)
```
Variable Scope
Variables created inside a function are destroyed once the function has executed.
The location (line of code) that you use a variable will determine its value.
Here n is 2 but inside my_function() n is 3.
So printing n inside and outside the function will determine its value.
```text
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
```text
def divide(n1, n2):
result = n1 / n2
```
#Option 1:
```text
divide(10, 5)
```
#Option 2:
```text
divide(n2=5, n1=10)
```
C O N D I T I O N A L S
If
This is the basic syntax to test if a condition is true. If so, the indented code will be executed, if not it will be skipped.
```text
n = 5
if n > 2:
print("Larger than 2")
```
Else
This is a way to specify some code that will be executed if a condition is false.
```text
age = 18
if age > 16:
print("Can drive")
else:
print("Don't drive")
```
Elif
In addition to the initial If statement condition, you can add extra conditions to test if the first condition is false.
Once an elif condition is true, the rest of the elif conditions are no longer checked and are skipped.
```text
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
```text
s = 58
if s < 60 and s > 50:
print("Your grade is C")
```
or
This expects either of the conditions either side of the or to be true. Basically, both conditions cannot be false.
```text
age = 12
if age < 16 or age > 200:
print("Can't drive")
```
not
This will flip the original result of the condition. e.g. if it was true then it's now false.
```text
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
```text
n = 1
while n < 100:
n += 1
```
For Loop
For loops give you more control than while loops. You can loop through anything
that is iterable. e.g. a range, a list, a dictionary or tuple.
```text
all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
print(fruit)
```
_ in a For Loop
If the value your for loop is iterating through, e.g. the number in the range, or the item in the list is not needed, 
you can replace it with an underscore.
```text
for _ in range(100):
#Do something 100 times.
```
break
This keyword allows you to break free of the loop. You can use it in a for or while loop.
```text
scores = [34, 67, 99, 105]
for s in scores:
if s > 100:
print("Invalid")
break
print(s)
```
continue
This keyword allows you to skip this iteration of the loop and go to the next. The loop will still continue, 
but it will start from the top.
```text
n = 0
while n < 100:
n += 1
if n % 2 == 0:
continue
print(n)
#Prints all the odd numbers
```
Infinite Loops
Sometimes, the condition you are checking to see if the loop should continue never becomes false. In this case, the loop will
continue for eternity (or until your computer stops it). This is more common with while loops.
```text
while 5 > 1:
print("I'm a survivor")
```
L I S T M E T H O D S
Adding Lists Together You can extend a list with another list by using the extent keyword, or the + symbol.
```text
list1 = [1, 2, 3]
list2 = [9, 8, 7]
new_list = list1 + list2
list1 += list2
```
Adding an Item to a List
If you just want to add a single item to a list, you need to use the .append() method.
```text
all_fruits = ["apple", "banana", "orange"]
all_fruits.append("pear")
```
List Index
To get hold of a particular item from a list you can use its index number.
This number can also be negative, if you want to start counting from the end of the list.
```text
letters = ["a", "b", "c"]
letters[0]
#Result:"a"
letters[-1]
#Result: "c"
```
List Slicing
Using the list index and the colon symbol you can slice up a list to get only the portion you want.
Start is included, but end is not.
```text
#list[start:end]
letters = ["a","b","c","d"]
letters[1:3]
#Result: ["b", "c"]
```
Range
Often you will want to generate a range of numbers. You can specify the start, end and step.
Start is included, but end is excluded: start <= range < end
```text
# range(start, end, step)
for i in range(6, 0, -2):
print(i)
# result: 6, 4, 2
# 0 is not included.
```
Randomisation
The random functions come from the random module which needs to be imported.
In this case, the start and end are both included start <= randint <= end
```text
import random
# randint(start, end)
n = random.randint(2, 5)
#n can be 2, 3, 4 or 5.
```
Round
This does a mathematical round.
So 3.1 becomes 3, 4.5 becomes 5 and 5.8 becomes 6.
```text
round(4.6)
# result 5
```
abs
This returns the absolute value.
Basically removing any -ve signs. 
```text
abs(-4.6)
# result 4.6
```
M O D U L E S
Importing
Some modules are pre-installed with python e.g. random/datetime
Other modules need to be installed from pypi.org
```text
import random
n = random.randint(3, 10)
```
Aliasing
You can use the as keyword to give your module a different name.
```text
import random as r
n = r.randint(1, 5)
```
Importing from modules
You can import a specific thing from a module. e.g. a function/class/constant
You do this with the from keyword.
It can save you from having to type the same thing many times.
```text
from random import randint
n = randint(1, 5)
```
Importing Everything
You can use the wildcard (*) to import everything from a module. Beware, this usually reduces code readability.
```text
from random import *
list = [1, 2, 3]
choice(list)
# More readable/understood
#random.choice(list)
```
C L A S S E S & O B J E C T S
Creating a Python Class
You create a class using the class keyword.
Note, class names in Python are PascalCased.
So to create an empty class
```text
class MyClass:
#define class
```

Creating an Object from a Class 
You can create a new instance of an object by using the class name + ()
```text
class Car:
    pass
my_toyota = Car()
```
Class Methods
You can create a function that belongs to a class, this is known as a method.
```text
class Car:
    def drive(self):
        print("move")
my_honda = Car()
my_honda.drive()
```
Class Variables
You can create a varaiable in a class.
The value of the variable will be available to all objects created from the class.
```text
class Car:
   colour = "black"
car1 = Car()
print(car1.colour) #black
```
The __init__ method
The init method is called every time a new object is created from the class.
```text
class Car:
    def __init__(self):
        print("Building car")
my_toyota = Car()
#You will see "building car"
#printed.
```
Class Properties
You can create a variable in the init() of a class so that all objects created from the class has access to that variable.
```text
class Car:
def __init__(self, name):
self.name = "Jimmy"
```
Class Inheritance
When you create a new class, you can inherit the methods and properties of another class.
```text
class Animal:
    def breathe(self):
        print("breathing")
class Fish(Animal):
    def breathe(self):
        super().breathe()
        print("underwater")
nemo = Fish()
nemo.breathe()
#Result:
#breathing
#underwater
```
