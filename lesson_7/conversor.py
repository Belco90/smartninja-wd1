# -*- coding: utf-8 -*-

print "Hello! This is a unit converter that converts kilometers into miles."

choice = 'yes'

while choice.lower() == "y" or choice.lower() == "yes":
    print "Please enter a number of kilometers that you'd like to convert into miles. Enter only a number!"
    km = raw_input("Kilometers: ")

    km = int(km)

    miles = km * 0.621371

    print "{} kilometers is {} miles.".format(km, miles)
    print "%s kilometers is %s miles." % (km, miles)
    print km + " kilometers is " + miles + " miles."

    choice = raw_input("Would you like to do another conversion (y/n): ")

print "Bye!"
