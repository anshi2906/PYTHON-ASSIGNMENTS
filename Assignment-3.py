#1. Write a python script to convert a number into str type.
from unicodedata import decimal


a=3
b=str(a)
print(b)
print(type(b))


#2. Write a python script to print Unicode of the character ‘m’
x='m'
print(ord(x))


#3. Write a python script to print character representation of a given unicode 100.
x=100
print(chr(x))


#4. Write a python script to print any number and its binary equivalent
x=2
print(bin(x))


#5. Write a python script to print any number and its octal equivalent.
a=3
print(oct(a))


#6. Write a python script to print any number and its hexadecimal equivalent.
a=4
print(hex(a))


#7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
x=0b1100101
print(int(x))


#8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
y=0x2F
print(oct(y))


#9. Write a python script to store an octal number 125 in a variable and print it in binary format.
z=0o125
print(bin(z))


'''10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format.'''
a=0o25
b=0x39
c=a+b
print(bin(c))