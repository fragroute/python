#!/usr/bin/python

name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_centimeters = height * 2.54
weight_in_kilograms = weight * 0.454
flot_number = round(1.7333)

print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "He's %d pounds heavy." %weight
print "Actually that's not too heavy."
print "He's got %s eys and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." %teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age,height,weight,age + height + weight)

print "He's %d centimeters tall." %height_in_centimeters
print "he's %d kilograms heavy." %weight_in_kilograms
print "Here is a flot number %f" %flot_number
