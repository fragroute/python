#!/usr/bin/python

x = "There are %d types of people." % 10 #declear a variable with formatted character as value
binary = "binary" #declear a variable with string as value
do_not = "don't"  #declear a variable with ' as value
y = "Those who know %s and those who %s." % (binary,do_not) #declear a variable with a string as value, the string which have two formatted characters

print x  
print y

print "I said: %r." % x #print variable x and %r will contains '' around the value of x
print "I also said: '%s'." % y #print variable x

hilarious = False  #declare a boolean variable
joke_evaluation = "Isn't that joke so funny?! %r" #declear a variable which value is a string contains formatted character.

print joke_evaluation % hilarious #print values of two variables

w = "This is the left side of..."
e = "a string with a right side."

print w + e #it's a string pinjie
