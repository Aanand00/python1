#use of print statement
print("1. Mix 500g of flour,10g Yeast and 300ml Water 1")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degree c for 30 minutes")


print('She said :"hello" and she left. ')
print("She said :'hello' and she left. ")
print("She said : \"hello\" and she left. ")
#string concatenation
print("anand\nanand\nanand\nanand")
print('Anand'+" "+'kumar'+" "+'jha')

# test by teacher
print('Day 1 - String Manipulation\nString Concatenation is done the "+" sign.')
print('e.g. print("hello " + " world")\nNew lines can be created with a backlash and n.')

#input function in python

#input("please enter your name")

print(' hello ' + input("please enter your name:"))

#try to find the length of the name provided by the user.

name= input('enter your name :')
print(len(name))
#if we want to  the same thing but in a single line of code then

print(len(input("enter your name")))

#varriables in python 

# varriables are the container that hold a data temporarily .

#try to switch the values between two variables given by user
a=input("input a number")
b=input("enter a number")
print(a)
print(b)
c=a
a=b
b=c
print('new value of a is:-' +a)
print('new value of b is-'+b)