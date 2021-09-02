# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:13:58 2021

@author: makbari19
"""
#%%Shortcuts and basic notes

# Python standard library:
# https://docs.python.org/3/library/functions.html

# pip automatically fetch packages released and listed on PyPI:
# https://pypi.org/

# Father is Guido van Rossum (a Dutch programmer) gave birth to python in 1991 

# Good book: https://jakevdp.github.io/PythonDataScienceHandbook/

# Good website to share codes: https://pastebin.com/

# Spyder is IDE

# Python is interpreter

# Shell is primary interface of python

# virtualenv is a virtual envirnomnt in which you modules are installed.

# pypi is python module repository

# in python everything is a object/entity/class which have attribute/metadata or function/method e.g.:
    # echa list has a append funtion L.append(100)
    # each integer a real and img attributes
# calling function of an object, you need to have () at the end
# calling attribute of an object, you do not have () at the end 

# =============================================================================

# Importing modules:
    
# import module as alias when using as: here numpy is namespace of the module and np is its alias
import numpy as np
# to access the attributes of module you need to define .
np.pi

# you can import module specific att/fun using from .... import ...: here you do not need to use .
pi # not defined 
from math import cos, pi
cos(pi)

# or import all:
from math import *
sin(pi) + cos(pi)

# importing all function/attributes of a module can cause problem.
# we have a built-in function of python as sum and also we have sum function in numpy so 
# both will have same name as sum(). to solve this, it is better to import them as below:
import numpy
help(sum)
help(numpy.sum)

# =============================================================================
# tools => preference =>shortkeys:
#     
# ctrl+1: commenting/uncommenting selected lines
# ctrl+4: commenting a block
# ctrl+5: uncommenting a block
# ctrl+enter for line by line run
# ctrl+alt+enter for all section run
# ctrl+enter in calculator activates help
# =============================================================================

# =============================================================================
# Magic commands or magic functions are one of the important enhancements that 
# IPython offers compared to the standard Python shell. These magic commands are 
# intended to solve common problems in data analysis using Python.  
# They are useful to embed invalid python syntax in the work flow.

# magic command for reset all variables; use only in consule (not script): %reset -f
# magic comand: "%pip install/uninstall" in console instead of cmd
# magic comand: %lsmagic in console to list magic command list

# >>> this means command prompt of python shell
# $ this is for linux terminal which is similar to cmd in windows

# space in start of lines matters but in middle it does not. 

# =============================================================================
# Code's table of content: View => pane=> outline

#%%Change directiory
import os

current_path = os.getcwd()

pyfile_path = 'C:/1.Research Files/1.Bibles/Python_Bibile/python_bible_spyder' #in python: '/'; in win: '\'

os.chdir(pyfile_path) 

os.path.isfile('age.json')  #check if a file exist or not

os.stat('age.json').st_size #check size of the file  

os.makedirs('new_folder_me') #creates new folder in current wd

#%% Data types:

# =============================================================================
# List, set and tuple:
A=[345,213,13,46,967,1]  #list is possible to modify

# concatinating list
A2 = A + [1,2,4]
# You cannot add a int to a list
A2 + 1
# for adding a number you should:
[a + 1 for a in A2]  

A2.sort()
A2

A = [1,2,3,4,5,6]
A[2]
A[0:4]
A[:4] 
A[:4] == A[0:4]
A[-3:]
A[0:len(A):2] #it means from first to last element by 2 as step size
A[::2]
A[0:len(A):2] == A[::2]

# =============================================================================
# Tuple is not possible to modify: tupple is immunable
B=(346,64,64,8)          
B[2]

# =============================================================================
# Set no repeat
a = {1,1,1,2}
print(a)
print(set([1,1,1,2]))

# Set operations:
prime = {2,3,5,7}
odd = {1,3,5,7, 9}
prime | odd
prime & odd
prime - odd

prime | odd == prime.union(odd)
prime & odd == prime.intersection(odd)
prime - odd == prime.difference(odd)

# =============================================================================
# dictionaty: dictionary is python is like json in javascript

classmates={'Tony':' cool but smells',
            'Jiji':' sits behind me'} # key : value

print(classmates)

print(classmates['Tony']) # calling by keys

for key, value in classmates.items():
    print(key + value)

#%% Control flow:

# =============================================================================
#for:
    
for x in range(10):
    print('Hi') #x is not in the loop so you can use _ instead in below 

for _ in range(10): # we just want looping with no iterator var
    print('Hi') 

for x in range(1,10,2):
    print(x) 

numbers = [1,2,3,4]

for i, num in enumerate(numbers):
    print(i,'number is: ',num)

# =============================================================================
# iterable variable:
# to show them, you should use *

a = range(10)
a
print(*a)

b = map(lambda x: x + 2, range(10))
b
print(*b)

c = zip([1,2,3], [10,4,56,7])
c
print(*c)

# you can have different iterable varaibles using itertools
from itertools import permutations
p = permutations(range(3))
print(*p) #or:
for val in p:
    print(val)

# =============================================================================
# List/set/dictionary/tuple comprehension:
[a + 2 for a in range(10) if a > 5]

[(i, j) for i in range(5) for j in range(4)]

{a % 3 for a in range(10000)} #mod of each number division to 3 is 0, 1 or 2

{n: n**2 for n in range(4)}

# =============================================================================

G = (n+2 for n in range(3))
#this is generator expression and it does not show unless we change it to list
# generator expression does not actually com‐
# pute the values until they are needed. This not only leads to memory
# efficiency, but to computational efficiency as well! This also means
# that while the size of a list is limited by available memory, the size of
# a generator expression is unlimited!
G
list(G) 
list(G) # it is used up after one call:
        # This can be very useful because it means iteration can be stopped and started

G = (n**2 for n in range(12))
for n in G:
    print(n, end=' ')
    if n > 30: break # here 1 to 36 are used up...

print("\ndoing something in between")

for n in G:
    print(n, end=' ')

# =============================================================================
# yield is same as return by it, in a function, produces generator.
def fun():
    return 1

a = fun()

def gen():
    yield  1

b = gen()
 
type(a)
type(b)  

print(a)        
print(b)    #no result for print, it is iterable so we need * to call it.   
print(*b)   #calling once, uses it up     
print(*b)   #so used up above ans show nothing
# =============================================================================
             
from itertools import count

# This is unlimited counter
count()

for i in count():
    print(i)
    if i>10: break

# =============================================================================
for n in range(10):
    print(all(n))
    print("me")

# =============================================================================
#while:
    
true = True
#By pass you pass and if statement but continue loop
#by continue, you come to start of loop
#by break, loop would be end
while true:
    a = int(input('give 1/2/3 value to break/pass/continue:'))
    if a == 2:
        
        pass
        
        print('Hi you passed')
    
    elif a == 3:

        print('You continue to start of while')

        continue
    
        print('This is not printed') #wen it reads continue, goes to start. this line is ignored
    
    else:
        print('You reached to end of while')
        break

# =============================================================================
# if:

a = 5
 
if a == 5: #instead on == use "is"
    print('a is 5')
elif a == 6:
    print('a is 6')
else:
    print('a is not 5')

#boolean operator (True/False) can be used in if

#%%Important notes:

# =============================================================================
# Boolean:
x = 3
(x>2) and (x<4) 
(x>2) or (x<4)
not (x>4)

# =============================================================================
a = [1,3,4,5,6]
5 in a
50 not in a

# =============================================================================
#float:
a = 1.25
a.as_integer_ratio() # or 5/4
numerator, denominator = a.as_integer_ratio() #similar to MATLAB
numerator
denominator 

# =============================================================================
# How to write a complex number:
a = 3 + 5j
a.real
a.imag
a.conjugate()
complex(3, 5) == 3 + 5j

# =============================================================================
a = 'Hi'
a*5
a + ' Mahdi' 

# =============================================================================
return_val = print('hi')
type(return_val)
print(return_val)

# =============================================================================
# bool of any number except zero is True
bool(0) 
bool("") 
bool("hello")
bool(-1) 
bool(1) 
bool(1014) 
bool(0.5)

# =============================================================================
aaa = 1; bbb = 2 #; this means next line

# =============================================================================
# Using triple """ to have multi line string: you do not need \n for next line. juste enter.
text = """
    hello this is Mahdi.
    this is text!
    This next line!
"""
print(text)
# =============================================================================
name='python'
print('Hello\n'+name)  #go to next line

# =============================================================================
#Place holder in print using %d:
a = 365
print('a is not %d!' %250)
print('a is %d!' %a)

# =============================================================================    
print('\'')            #using \ for printing special charechter like quotation
print('she said "don\'t do that"')

print('a',1)
print('a'+1)
print('a '+str(1))

# specific printing
print('\033[46m' + 'Hi') #colored print and more in: https://www.google.com/search?q=%5C033%5B91m&rlz=1C1GCEB_enFI852FI852&sxsrf=ALeKk02AEeD-h97GtxVNyuM4hpRTxRVrNg:1608567425702&tbm=isch&source=iu&ictx=1&fir=7tG53I_2D8fWPM%252CTRSbEL-LidPhXM%252C_&vet=1&usg=AI4_-kQuwf3xP4ZPohrfAUew5SixxEZcww&sa=X&ved=2ahUKEwiE04XQvN_tAhXNxIsKHYL7DHEQ9QF6BAgMEAE#imgrc=7tG53I_2D8fWPM
print('\033[46m' + 'Hi' + '\033[0m')
print('\033[92m' + 'Hi' + '\033[0m')

print(1,2,3, sep = '___')

# =============================================================================
food=('A','B','C')
food[:2] #means from first to 2 so 0, 1

# finding, replace an index functions of a string
name = 'Ali'
print(name.index('i'))

# =============================================================================
# input from user:
beautiful_number = input("tell me a beautiful number:")

# =============================================================================
# How to use range:

range(1, 10, 2) # this is iterable and can be used in loops. 

list(range(1, 10, 2)) # we can change it to list

# =============================================================================
# zipping:
a = [1, 2, 3]
b = ['a', 'b', 'c']

type(a)

ab = list(zip(a, b)) #making a zipped var visible
ab

for a, b in zip(a, b):
    print(b, a)

# =============================================================================
stock={
    'goog':520.54,
    'fb':76.45,
    'yho':39.28,
    'amz':306.21,
    'appl':99.76
}

#Sorting a dictionary by value or keys: first we should zip it

dic={
    'a':234,
    'b':3432,
    'c':345,
    'd':23
}

print(min(dic)) #but it is min one between keys in alphabetical order
print(min(dic.values())) #we want to know which key has the lowest values so we should zip them
                         # so that we can have tuple from (value, key)
print(min(zip(dic.values(),dic.keys())))

# Dictionary Multiple Key Sort
user=[
     {'fname':'a1','lname':'a2'},
     {'fname':'b1','lname':'b2'},
     {'fname':'d1','lname':'d2'},
     {'fname':'c1','lname':'c2'}
]

sorted(user, key = lambda item: item['fname'])

# or:
from operator import itemgetter

for x in sorted(user, key = itemgetter('fname')):
     print(x) #look at last two variables, name is correct but lname needs sorts as well
print('----------')
for x in sorted(user, key = itemgetter('fname','lname')): #so now it sorts by fname then by lname
     print(x) #look at last two variables, name is correct but lname needs sorts as well
     
# =============================================================================
    
#how to use "in":
groceries=('A','B','C','D','E','F')

if 'A' in groceries:
    print('You have A')
else:
    print('Buy A')

# =============================================================================

sample='Ali1,Ali2 \\nGhasem1,Ghasem2\\nAhmad1,Ahmad2' #the first slash helps to have special char. 
sample_split1=sample.split(',')
sample_split2=sample.split('\\n') #this is good for detecting number of lines in csv files. use \\n!
print(sample)
print(sample_split1)
print(sample_split2)
len(sample_split1)
len(sample_split2)

# =============================================================================

a=['ali']
a.append('hali') #a should be list. it adds new arg with no need to define new variable
print(a)
word='ali'
ref='ab'
word.replace(ref[0],'c') #word should be string not list

# =============================================================================

item=['december 23, 2015', 'bread gloves', 8.51]
print(item[0])

date, item, price=['december 23, 2015', 'bread gloves', 8.51] #we have three variables in list so we should have three names before list

print(date)
print(item)
print(price)

date, *item, price=['december 23, 2015', 'bread gloves1', 'bread gloves2', 'bread gloves2', 8.51] #if you use *, it will cover all extra variables inside the list

print(date)
print(item)
print(price)
# =============================================================================
#finding most frequent item in a list
from collections import Counter

text='Text messaging, or texting, is the act of composing and sending electronic messages, typically ' \
     'consisting of alphabetic and numeric characters, between two or more users of mobile devices, ' \
     'desktops/laptops, or other type of compatible computer. Text messages may be sent over a cellular ' \
     'network, or may also be sent via an Internet connection.'

words=text.split()

print(words)

counter = Counter(words)

top_three = counter.most_common(3)

print(top_three)

for word, count in top_three:
    print(word)
# =============================================================================
# smallest in a list
import heapq

grades=[10,12,234,123,123,4325,334643]

print(heapq.nlargest(3,grades)) #it gives your three biggest numbers from grades

stocks=[
    {'company': 'a', 'price':123},
    {'company': 'b', 'price':343},
    {'company': 'c', 'price':234}
]

stocks[1].keys()
stocks[1].values()
stocks[1]['price']
stocks[1]['company']

print(heapq.nsmallest(2, stocks, key = lambda x: x['price']))

# =============================================================================
#Sorting a dictionary:
from operator import attrgetter


class User:
    def __init__(self, x, y):
        self.name = x
        self.id = y

    def __repr__(self):  # it tells python to represent what when the object is called
        return self.name + ':' + str(self.id)


Users_mahdi = [
    User('ac00', 10),
    User('add20', 11),
    User('ab11', 12),
    User('ab11', 10)
]

for i in Users_mahdi:
    print(i)
print('__________')
for i in sorted(Users_mahdi, key=attrgetter('id')):
    print(i)
print('__________')
for i in sorted(Users_mahdi, key=attrgetter('name')):
    print(i)
print('__________')
for i in sorted(Users_mahdi, key=attrgetter('name', 'id')):
    print(i)

# =============================================================================
# Date:
import datetime
import humanize

now = datetime.datetime.now()
desire = datetime.datetime(1991, 3, 14)

humanize.naturaltime(now - desire)

# =============================================================================
# Bitwise operator:
    # each 8 bits = 1 byte: 2^7,2^6,2^5,2^4,2^3,2^2,2^1,2^0
    # 50 = 32 + 16 + 2 = 2^5 + 2^4 + 2^1 : 00110010 is binary of 50

print(bin(50))
print(bin(25))

c = 50 & 25 # 110010 & 011001=010000 =>2^4=16
d = 50 | 25

print(c)
print(d)

x=240    #byte of it is 11110000

y = x >> 2 #shifts bits by 2 which will be: 00111100 which is 4+8+16+32=60

print(y)

# =============================================================================

# The all() function is an inbuilt function in Python which returns true if 
# all the elements of a given iterable( List, Dictionary, Tuple, set, etc) are True 
# else it returns False. 
# It also returns True if the iterable object is empty.

l = [4, 5, 1]
print(all(l))

l = [0, 0, False]
print(all(l))

l = [1, 0, 6, 7, False]
print(all(l))

l = []
print(all(l))


p = list(range(1,10))
p

[16 % a > 0 for a in p] # false if number is not dividable to 16
all([16 % a > 0 for a in p]) # it is false because all numbers in the list are not dividable to 16

# compare it to any
p = list(range(1,10))
any([16 % a > 0 for a in p])
#%% Functions

# =============================================================================

a = 123 #a is a global var
def core():
    print(a)

core()

b = 124

def core():
    
    a = 456 #a is a local var
    
    global b #if type this, inside function, you have access to vars from outside
    
    print(a + b)

core()

# =============================================================================

def my_function(name='default name',age='default age'): #dont use MyFunction, it is for classes
    print('My name is '+ str(name)+ ' and my age is '+ str(age))

my_function() #if you do not enter new values for arguments, it will use default arguments
my_function('mahdi')
my_function('mahdi',29)
my_function(None,29)

# =============================================================================
def add_nums(*x): #x can be any set of numbers
    
    total=0
    
    for a in x:
        
        total = total + a
        
    print(total)

add_nums(3,2,4,6)

# =============================================================================
# *args ans **kwargs: 
    # first one is when you do not know the length of input arguments as list
    # second one is when you do not know the length of input arguments as dictionary
    
def fun_me(*args, **kwargs):
    
    list_input = args
    
    dic_input = kwargs
    
    print(list_input)
    print(dic_input)
    
    return dic_input['b'] * (sum(list_input) + dic_input['a'])

# Please note that how nicely, args/kwargs are changed to a united list/dictionary automatically.
fun_me(1, 2, 3, a = 3, b = 10)

# OR EQUIVALLENTYLY:
list_input = [1,2,3]
dic_input = {'a':1, 'b':10}
fun_me(*list_input, **dic_input)

# =============================================================================

def drop_first_last(grades): #this gets average only from middle grades, not all grades. 
    
    first, *middle, last = grades

    ave = sum(middle)/len(middle)

    print(middle)

    print(ave)

drop_first_last([65,76,98,54,21])

# =============================================================================
def health_calc(age,apple_ate,cig_amoked): #it needs three arguments
    answer=100-age+apple_ate*1.5-cig_amoked*2
    print(answer)

mahdi_data=[20,12,0]
health_calc(mahdi_data[0],mahdi_data[1],mahdi_data[2])
health_calc(*mahdi_data) #using asterisk summarize the coding but its logic is same as above line

# =============================================================================

#%% "lambda" (anonymous function) and "map"
# lambda is like handdle in Matlab
# map is like apply in R

answer = lambda x: x*7

print(answer(3))

income=[[20, 10], [50, 10]]

list(map(lambda x: x*2, income))
list(map(lambda x: x*2, [10, 20, 30]))

# =============================================================================
# it can generate true false:
is_even = lambda x: x%2 == 0
is_even(2)
is_even(3)

# =============================================================================
# How to use filter:

for val in filter(is_even, range(10)):
    print(val)
#%% Read and write files

fw = open('sample.txt','w+') #here you can read and write

#here you just open the text file. to read it, use fw.read()
#you DO NOT need to have sample.txt file. when you open and then close it, it is created. 

fw.write('writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close() #it will be saved in py file directory
 
fr = open('sample.txt','r') # here you can just read
text = fr.read()
print(text)
fr.close()



#%% Exception handle:

# Different types of syntax errors:
    #1. syntax error
    #2. runtime error: easy to solve, when input is not given by user properly
    #3. semantic error: code executes without error but logically it has error. to solve it:

def divide_me(a, b):
    try:
        return a/b
    except ZeroDivisionError: #we here only capture zerodivision error and let all go below
        return 2000
    except:
        print('INPUT IS NOT OK!')
        
divide_me(1,2)
divide_me(1,0)
divide_me(1,'0')


try: #its for when everything is ok and number is enterd...
    number=int(input('what is your fav number?\n'))
    print(18/number)
except ValueError: #what if text is entered by user?
    print('you did not enter a number. DUDE!')
except ZeroDivisionError:
    print('zero is not allowed')
else:
    print('I will be run if the try is executed successfully')
finally: #regardless of above options, finally would be run in each loop!
    print('I will be run in any case!')

# How to use raise: it shows the message you mentioned inside ()
number = 'a'
if type(number) is str:
    raise TypeError('This is TypeError by Mahdi Joon!')
else:
    print(2 + number)
#%% Local modules: module and main file should be in same directory

#0.make new project in the directory. it will redirect wd to project main py file
#1.make a classes folder and new __init__.py file in it then
#1.2.copy your local modules in classes folder
#2.in each module you can have function or classes.
#3.import module by import command
#4.if you change you module py file and save it. Then, 
#4.1.call in main py file, it will apply changes there as well.

#5.import it:

from classes import Module 

from classes import function_mahdi 

function_mahdi.function_me(1, 2)

#5.1.or using relative address: in class folder, we have function_mahdi which as function_me 

from classes.function_mahdi import function_me as fun

fun(1, 2)

function_me = Module.hello_fun()
 
flipper = Module.Tuna(10,5) #when calling class, you need to define dynamic vars

flipper.b
flipper.life
flipper.age 
flipper.name_age

flipper.fish() #fish is a function so you need to have "()" 
flipper.swim()
flipper.attack() #this has error since input is not defined. 
flipper.attack(100)

#%% String cool manupulations:
fox = "tHe qUICk bROWn fOx."
# beside fox.lower() or fox.upper(), we have:
fox.title()
fox.capitalize()    
fox.swapcase()

line = '         this is the content         '
line.strip()

num = '00000045'
num.strip('0')

# =============================================================================

line = "this is the content"
line.center(30)
line.ljust(30)
line.rjust(30)

'435'.rjust(10, '0')

# zero filling is common in python so instead of above comand by rjust, you can use zfill
'435'.zfill(10)

# =============================================================================

#find and replace are function of each string variable in python:

# find is like index in a list. list does not have find but string has index

# The only difference between find() and index() is their behavior
# when the search string is not found; find() returns -1, while
# index() raises a ValueError
  
string = "Hi this is me!"

string.find('Hi')
string.index('Hi')

string.index('Hii')

string.find('boo')
string.index('boo')

string.replace('Hi', 'Bye')
string.replace('hi', 'Bye') # it is case sensitive

# partitioning text to before and after a word
string.partition('this')

string.split()

text = """Hello,
this is my text
how are you
so bye bye
"""

text.splitlines()

"--".join(['1','2','3'])

# =============================================================================
# how to replace 
"I am {}".format('cool')

"I am {0} and {1}".format('cool', 'brave')

"I am {a} and {b}".format(a = 'cool', b = 'brave')

keyarg = {'a':'cool', 'b': 'brave'}

"I am {a} and {b}".format(**keyarg)

from math import pi
"pi is {0:.3f}".format(pi)
"pi is {0:.4f}".format(pi)

#%% PIL Module: conda install pillow

import Requests
from io import BytesIO
from PIL import Image

#UDEMY:

r = requests.get('https://images.pexels.com/photos/799443/pexels-photo-799443.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500')
r.status_code # if 200, retrieving is working ok

image = Image.open(BytesIO(r.content)) #ytesIO makes r.content possible to be readable by Image.open

image.size
image.mode
image.format

try:
    image.save('image.jpg', image.format)
except IOError:
    print('I cannot save!')

# =============================================================================
  
#New Boston:

img = Image.open('459.jpg')

print(img.size)

print(img.format)

img.show() #it opens in photoshop

#cropping image:
area=(100,100, 300, 375) #starting point of crop from top left to down right
cropped=img.crop(area)
cropped.show()

#combining images:
image2=Image.open('2.png')
image1=Image.open('1.png')
#this is the location of the overlaying image (image1:280*272) in base image (image2:407*305) from top left to bottom right:
area= (50 , 50 , 50+280 , 50+272)
image2.paste(image1 , area)
image2.show()

#breaking up image to RGB:
#each cell of a picture is combination of three colors: RGB
image=Image.open('image.jpg')
print(image.mode) #it says your image is RGB or not because we have 4 color images as well.
r, g, b = image.split()
r.show()
b.show()
g.show()

new_image=Image.merge('RGB', (r,g,b))
new_image.show()

new_image=Image.merge('RGB', (b,g,r))
new_image.show()

image1=Image.open('image.jpg')

image2=Image.open('image2.jpg')

r1, g1, b1 = image1.split()
r2, g2, b2 = image2.split()

new_image=Image.merge('RGB', (r1,g2,b1)) #the size of two images shall be same
new_image.show()

# Basic transformations on image

image=Image.open('image.jpg')
image.show()

square_image=image.resize((250,250)) #the size of the image is arq. of the resize
square_image.show()
flip_image=image.transpose(Image.FLIP_LEFT_RIGHT)
flip_image.show()
spin_image=image.transpose(Image.ROTATE_90)
spin_image.show()

# Filters:
from PIL import ImageFilter
image=Image.open('image.jpg')
image.show()

#convert RGB to black and white
image2=image.convert('L')
image2.show()

#other converts
image2=image.filter(ImageFilter.BLUR)
image2.show()
#detail is opposite of blur
image3=image.filter(ImageFilter.DETAIL)
image3.show()
image4=image.filter(ImageFilter.FIND_EDGES)
image4.show()

#%%Requests Module

#Here is from Udemy

import requests

#you can get data from a url
#when searching for pizza in google, url cahnges to: https://www.google.com/search?q=pizza

params = {"q": "pizza"} 

r = requests.get('http://www.google.com/search', params = params)

r.status_code #200 means ok request

r.url

r.text # content of the url

r.headers
r.headers['Date']

#saving a page:
f = open('page.html', 'w+', encoding="utf-8")
f.write(r.text)
f.close()

# you can also post iformation like name and email to a url:

my_data = {'name': 'mahdi',
           'email':'asdf@gs.co'}  
  
r = requests.post('sample.com', data = my_data)

f = open('page2.html', 'w+')
f.write(r.text) #it will show you same page as you enter your name and email in sample.com

#%%Beatiful Soap Module 
      
#To check project, CHECKkkkkkkkkkkkkkkk webscrapery folder....

#it works for requesting info from net web pages
#it sorts webpage data. it gets special format of data

from bs4 import BeautifulSoup 

#Web crawler (session 25-27 of new boston)
#the main note in this section is:
#right click on a specific element in a webpage and browse it.
#you can call it by its class and so on...

# for digikala
def trade_spider(max_pages):
    page=1
    while page <= max_pages:
        url='https://www.digikala.com/search/?q=sony&pageno='+str(page)+'&sortby=22' #I chose digikala
        source_code=requests.get(url) #it gets source code of the webpage. you get manually by right click of the page in browser as well
        plain_text=source_code.text #it takes only text of the source code
                                    #we have diff craps in a source code and here only we need texts of it!
        soup=BeautifulSoup(plain_text) #it convert plaintext to specific format of BS4 module
        for link in soup.findAll('a',{'class','js-product-url'}): #findAll will determine all links ('a' means link) in soup object and detemined all class ='data-title-fa' (this is from webpage source inspected from browser).
            href='https://www.digikala.com/'+link.get('href') #you can get any property you want from link
            id=link.get('data-adro-ad-click-id')              #I want product id from webpage source
            title=link.string   #the only think in link as string is the title of the product so you can call it
            print(href)
            print(title)
            print(id)
        page+=1

#this goes inside a specific link and generated its title:
def get_single_item(item_url):
    source_code=requests.get(item_url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text)
    for item_name in soup.findAll('h1',{'class':'c-product__title'}):
        print(item_name.string) #it print the title of the page
    for link in soup.findAll('a'): #it gives anything as a link in url
        href=link.get('href')
        print(href)
# =============================================================================

url_manual='https://www.digikala.com/product/dkp-914908/%DA%A9%D9%86%D8%B3%D9%88%D9%84-%D8%A8%D8%A7%D8%B2%DB%8C-%D8%B3%D9%88%D9%86%DB%8C-%D9%85%D8%AF%D9%84-playstation-4-slim-%DA%A9%D8%AF-region-2-cuh-2216a-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-500-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA'
get_single_item(url_manual)

#%%REGEX Module

import re

string='hi, this is Mahdi/.123'

#you can substitute whithin a string. 
#first arqument is what you dont want and second is substitution.

new_str=re.sub('[.,/A-Z" "[0-9]', 'Z', string)

new_str

# +" " means space and A-Z means all capital letters and +[0-9] means all numbers.

string='hi. 123'

new_str=re.sub('[^0-9]', 'X',string) #^[0-9] means all except numbers

new_str
#%%Data Visualization 
#%%%Timeseries:
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

y2 = [a + 10 for a in y]

l1 = plt.plot(x, y, '--', color = (0, 0.1, 0.1))
l2 = plt.plot(x, y2, color = (0, 0.5, 0.1))

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Title')

plt.grid()

plt.setp(l1, marker = '*')
plt.setp(l2, marker = 'o')

plt.show()

#%%%Piecharts:
    
import matplotlib.pyplot as plt

labels = 'a','b','c','d'
size = [1,2,3,4]
separte = [0.1,0,0,0] #it means separte a but not others: using bigger number instead of 0.1, separate more

plt.pie(size, labels = labels, autopct= "%1.1f%%", explode=separte)
plt.axis('equal')

plt.show()

#%%%Pandas and matplot
#good summary of pd: https://lifeodyssey.github.io/posts/da4a7e8b.html
    
import matplotlib.pyplot as plt
import pandas as pd

#format of data should be like below to pass it in dataframe:
data = {'col1':[1,2,3],
        'col2':[10,20,30],
        'col3':['a','b','c'],
        'col4':['a','b','c']}

df = pd.DataFrame(data, columns = ['col1','col2','col3']) #even you can select some of cols here

df['col_new'] = df['col1'] + df['col2']

plt.pie(df["col_new"],
        labels = df['col3'],
        colors = ['red','blue','green'],
        autopct='%1.1f%%') 

#%%%Barplot
    
import matplotlib.pyplot as plt
import numpy as np

a = [10, 20, 30, 40]
b = list(map(lambda x: x-5, a))
c = [i-10 for i in b]
d = [10, 20, 30, 40]

index = np.arange(4)
bar_width = 0.2

print(index)

bar_a = plt.bar(index, a, bar_width, label = 'a') #it means that x location of bars is from index
bar_b = plt.bar(index + bar_width, b, bar_width, label = 'b')
bar_c = plt.bar(index + 2*bar_width, c, bar_width, label = 'c')

#accessing elemnts of the bar plot and labeling bar plots by them:
for item in bar_a:
    print(item.get_x(), item.get_height(), item.get_width())
    
    plt.text(item.get_x() + item.get_width()/2, 
             item.get_height() * 1.05,
             '%d' %int(item.get_height()),
             ha = 'center')
#to make it more nice, you can change above for to a function and call it.
def Fun_labeling(bar_plot):
    for item in bar_plot:   
        plt.text(item.get_x() + item.get_width()/2, 
                 item.get_height() * 1.05,
                 '%d' %int(item.get_height()),
                 ha = 'center')
        
Fun_labeling(bar_b)
Fun_labeling(bar_c)

plt.grid()
plt.legend()
plt.xticks(index + bar_width / 2, ('math','physics','philosophy','sport'))
plt.ylabel('y')
plt.xlabel('x')

plt.text()
plt.show()