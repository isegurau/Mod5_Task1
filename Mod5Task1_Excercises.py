#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Interactive Mode
#three greater-than signs (>>>); for continuation lines 
the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")


# In[ ]:


#Source Code Encoding
# -*- coding: encoding -*-

# to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:
# -*- coding: cp1252 -*-


# In[8]:


# 3 An Informal Introduction to Python# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."


# In[18]:


#numbers
2 + 2


# In[17]:


50 - 5*6


# In[19]:


(50 - 5*6) / 4


# In[20]:


8 / 5  # division always returns a floating point number


# In[21]:


17 / 3  # classic division returns a float


# In[22]:


17 // 3  # floor division discards the fractional part


# In[23]:


17 % 3  # the % operator returns the remainder of the division


# In[24]:


5 * 3 + 2  # result * divisor + remainder


# In[25]:


#squared
5 ** 2  # 5 squared


# In[26]:


2 ** 7  # 2 to the power of 7


# In[27]:


#The equal sign (=)
width = 20
height = 5 * 9
width * height


# In[28]:


n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>


# In[29]:


4 * 3.75 - 1


# In[30]:


tax = 12.5 / 100
price = 100.50


# In[31]:


price * tax


# In[32]:


#In interactive mode, the last printed expression is assigned to the variable _ 
price + _


# In[33]:


round(_, 2)


# In[34]:


#Strings
'spam eggs'  # single quotes


# In[35]:


'doesn\'t'  # use \' to escape the single quote...


# In[36]:


"doesn't"  # ...or use double quotes instead


# In[37]:


'"Yes," they said.'


# In[38]:


"\"Yes,\" they said."


# In[39]:


'"Isn\'t," they said.'


# In[40]:


#The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters
print('"Isn\'t," they said.')


# In[41]:


s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output


# In[42]:


print(s)  # with print(), \n produces a new line


# In[43]:


print('C:\some\name')  # here \n means newline!


# In[44]:


#If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print(r'C:\some\name')  # note the r before the quote


# In[45]:


#String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string
print("""Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# In[46]:


#Strings can be concatenated (glued together) with the + operator, and repeated with *:
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'


# In[48]:


#concatenate
'Py' 'thon'
'Python'


# In[49]:


#This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')
text


# In[5]:


prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
    prefix 'thon'


# In[7]:


#If you want to concatenate variables or a variable and a literal, use +
prefix = 'Py'
prefix + 'thon'


# In[8]:


#Strings can be indexed (subscripted)
word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5


# In[9]:


#Indices may also be negative numbers, to start counting from the right (start from -1.)
word[-1]  # last character
word[-2]  # second-last character
word[-6]


# In[11]:


#Obtain substring
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:6]


# In[15]:


#Note how the start is always included, and the end always excluded
word[:2] + word[2:]

word[:4] + word[4:]


# In[16]:


#Slice indices have useful defaults; an omitted first index defaults to zero
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end


# In[17]:


#Attempting to use an index that is too large will result in an error
word[42]


# In[18]:


#out of range slice indexes are handled gracefully when used for slicing:
word[4:42]
word[42:]


# In[19]:


#Python strings cannot be changed — they are immutable.
word[0] = 'J'


# In[20]:


#If you need a different string, you should create a new one:
'J' + word[1:]

word[:2] + 'py'


# In[21]:


#The built-in function len() returns the length of a string:
s = 'supercalifragilisticexpialidocious'
len(s)


# In[25]:


#LISTS  - Lists might contain items of different types, but usually the items all have the same type.
squares = [1, 4, 9, 16, 25]
squares


# In[27]:


#lists can be indexed and sliced
squares[0]  # indexing returns the item
#1
squares[-1]
#25
squares[-3:]  # slicing returns a new list
#[9, 16, 25]

squares[:-3]  # slicing returns a new list
#[9, 16, 25]


# In[28]:


#A copy of the list:
squares[:]


# In[29]:


#Lists also support operations like concatenation:
squares + [36, 49, 64, 81, 100]


# In[32]:


#lists are a mutable type,it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
#64
cubes[3] = 64  # replace the wrong value
cubes


# In[33]:


#Add new items at the end of the list
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes


# In[34]:


#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
#['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
#['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters
#['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters


# In[35]:


#Len function also works with lists
letters = ['a', 'b', 'c', 'd']
len(letters)


# In[1]:


#It is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
[['a', 'b', 'c'], [1, 2, 3]]
x[0]
['a', 'b', 'c']
x[0][1]
'b'


# In[2]:


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


# In[4]:


#Use of Print:
i = 256*256
print('The value of i is', i)


# In[5]:


#Use of Print:
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b


# In[6]:


#4 - if Statements
x = int(input("Please enter an integer: "))
#Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# In[7]:


#for Statements
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# In[37]:


#The range() Function
for i in range(5):
    print(i)


# In[38]:


#To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# In[40]:


print(range(10))


# In[43]:


sum(range(4))  # 0 + 1 + 2 + 3


# In[44]:


#get a list from a range. 
list(range(4))


# In[1]:


#break and continue Statements, and else Clauses on Loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# In[2]:


#The continue statement, also borrowed from C, continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


# In[ ]:


#The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# In[ ]:


#This is commonly used for creating minimal classes:
class MyEmptyClass:
    pass


# In[ ]:


#Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level
def initlog(*args):
    pass   # Remember to implement this!


# In[3]:


#Defining Functions
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)


# In[8]:


#The value of the function name has a type that is recognized by the interpreter as a user-defined function. This value can be assigned to another name which can then also be used as a function. 
fib
f = fib
f(100)


# In[7]:


fib(0)
print(fib(0))
None


# In[3]:


#It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100     


# In[6]:


#More on Defining Functions
#Default Argument Values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[14]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[8]:


#the following function accumulates the arguments passed to it on subsequent calls:
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[11]:


#If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# In[18]:


# Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# In[21]:


#but all the following calls would be invalid:
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument


# In[22]:


def function(a):
    pass

function(0, a=0)


# In[23]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[24]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# In[30]:


#Special parameters - Function Examples
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# In[31]:


#The first function definition, standard_arg, the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword:
standard_arg(2)

standard_arg(arg=2)


# In[34]:


#The second function pos_only_arg is restricted to only use positional parameters as there is a / in the function definition:
pos_only_arg(1)
pos_only_arg(arg=1)


# In[39]:


#The third function kwd_only_args only allows keyword arguments as indicated by a * in the function definition:
kwd_only_arg(3)

kwd_only_arg(arg=3)


# In[41]:


#And the last uses all three calling conventions in the same function definition:
combined_example(1, 2, 3)

combined_example(1, 2, kwd_only=3)


combined_example(1, standard=2, kwd_only=3)


combined_example(pos_only=1, standard=2, kwd_only=3)


# In[42]:


def foo(name, **kwds):
    return 'name' in kwds


# In[43]:


#Recap
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):


# In[44]:


#Arbitrary Argument Lists
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[49]:


def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'


# In[50]:


#Unpacking Argument Lists
list(range(3, 6))            # normal call with separate arguments
args = [3, 6]
list(range(*args))           # call with arguments unpacked from a list


# In[51]:


#In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# In[55]:


#Lambda Expressions -  anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. 
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)


# In[56]:


#The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


# In[58]:


#Documentation - The first line should always be a short, concise summary of the object’s purpose. should begin with a capital letter and end with a period.
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


# In[60]:


#Function Annotations - Return annotations are defined by a literal ->, followed by an expression, between the parameter list and the colon denoting the end of the def statement.
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')


# In[62]:


#5. Data Structures
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
#2
fruits.count('tangerine')
#0
fruits.index('banana')
#3
fruits.index('banana', 4)  # Find next banana starting a position 4
#6
fruits.reverse()
fruits
#['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
#['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
#['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
#'pear'


# In[64]:


#Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
[3, 4, 5, 6, 7]
stack.pop()
#7
stack
#[3, 4, 5, 6]
stack.pop()
#6
stack.pop()
#5
stack
#[3, 4]


# In[66]:


#Using Lists as Queues (FIFO)
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
#'Eric'
queue.popleft()                 # The second to arrive now leaves
#'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])


# In[67]:


#List Comprehensions - consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses
squares = []
for x in range(10):
    squares.append(x**2)

squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# In[69]:


# We can calculate the list of squares without any side effects using:
squares = list(map(lambda x: x**2, range(10)))
squares
squares = [x**2 for x in range(10)]
squares


# In[70]:


#this listcomp combines the elements of two lists if they are not equal:
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[71]:


#and it’s equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs


# In[73]:


#If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]
#[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
#[0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec]
#[4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
#['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
#[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
#[1, 2, 3, 4, 5, 6, 7, 8, 9]


# In[74]:


#List comprehensions can contain complex expressions and nested functions:
from math import pi
[str(round(pi, i)) for i in range(1, 6)]
#['3.1', '3.14', '3.142', '3.1416', '3.14159']


# In[77]:


#Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
#The following list comprehension will transpose rows and columns:
[[row[i] for row in matrix] for i in range(4)]
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


# In[78]:


#As we saw in the previous section, the nested listcomp is evaluated in the context of the for that follows it, so this example is equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed


# In[79]:


#which, in turn, is the same as:
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed


# In[80]:


#The zip() function would do a great job for this use case:
list(zip(*matrix))


# In[81]:


#The del statement -  used to remove slices from a list or clear the entire list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
#[1, 66.25, 333, 333, 1234.5]
del a[2:4]
a
#[1, 66.25, 1234.5]
del a[:]
a
#[]


# In[83]:


#del can also be used to delete entire variables:
del a
a


# In[84]:


#Tuples and Sequences - A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
t[0]
#12345
t
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
#((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v


# In[85]:


# a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses)
empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)
0
len(singleton)
1
singleton
#('hello',)


# In[87]:


#sequence unpacking 
t = 12345, 54321, 'hello!'
x, y, z = t


# In[88]:


#Sets - A set is an unordered collection with no duplicate elements
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
#{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # fast membership testing
True
'crabgrass' in basket
False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}


# In[89]:


# set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}
a


# In[90]:


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
#{'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
#4098
del tel['sape']
tel['irv'] = 4127
tel
#{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
#['jack', 'guido', 'irv']
sorted(tel)
#['guido', 'irv', 'jack']
'guido' in tel
#True
'jack' not in tel


# In[91]:


#The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


# In[92]:


#dict comprehensions can be used to create dictionaries from arbitrary key and value expressions
{x: x**2 for x in (2, 4, 6)}


# In[93]:


#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
dict(sape=4139, guido=4127, jack=4098)


# In[94]:


#Looping Techniques - items() method
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


# In[96]:


#using the enumerate() function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# In[97]:


#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# In[98]:


#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function
for i in reversed(range(1, 10, 2)):
    print(i)


# In[100]:


#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


# In[101]:


#It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data


# In[102]:


#More on Conditions
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null


# In[ ]:


#Comparing Sequences and Other Types

