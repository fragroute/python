from sys import argv  #import a module which named argv

script,filename = argv #read input and assign them to the variables

txt = open(filename)   #use function open a file from input

print "Here's your file %r:" % filename   #print the filename
print txt.read()             #call a function on txt named read, and print the content

#print "Type the filename again:"  
#file_again = raw_input(">")      #read filename from input and prompt user with ">"

#txt_again = open(file_again)    #open a file which 
#print txt_again.read()           #print the content which read from the file
