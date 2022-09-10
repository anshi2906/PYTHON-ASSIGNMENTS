#1.Write a python script to add comments and print “Learning Python” on screen.
print('''"Learning Python"''')          #adding comment using # symbol


#2.Write a python script to add multi line comments and print values of four variables,each in a new line. Variable contains any values.
'''we can add 
multi line comments 
using triple quots'''
a="Anshi"
b="Rudrapur"
c=2
d=2.3
print(a,b,c,d,sep="\n")


'''3.Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)'''
x=35
y=True
z="MySirG"
s=5.49
r=3+4j
print(type(x))
print(type(y))
print(type(z))
print(type(s))
print(type(r))


#4.Write a python script to print the id of two variables containing the same integer values.
a=7
b=7
print(id(a))
print(id(b))


'''5.Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable'''
a='anshi'
b=20
c=21.3
d=4+4j
print(type(a),id(a))
print(type(b),id(b))
print(type(c),id(c))
print(type(d),id(d))


#6.Write a python script to print all the keywords
import keyword
print(keyword.kwlist)


'''10.Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)'''
from datetime import date
today=date.today()
print(today)

from datetime import time
a=time(12,24,36)
print(a)