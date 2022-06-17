#****************************************************************
#Name: Goodnews Agbadu
#Student Number: A00238219
#
#ANA1001 Lab 1
#****************************************************************

#Question #1 Four programs I would like to create using comments:

"""I would love to create a risk profile program, free games for kids, online calculator, universal tv remote and a new digital currency code."""

#Question #2
#Assiging sharon to the variable (a) and print it:
a = "sharon"
print(a)
#Assigning thuc to the variable (a) and formating the output using .title:
a = "thuc"
print(a.title())
#Assigning Pradip to the variable (a) and formating the output using .upper:
a = "pradip"
print(a.upper())

#Question #3
#Assigning Goodnews to the variable (x)
x = "goodnews"
#Printing out X within a sentence using an f string:
print(f"my name is {x}" ".")
#Modifying name to show in Uppercase, Lowercase and title case three times:
print(f"{x.upper()} is a good name.")
print(f"{x.lower()} is a good name.")
print(f"{x.title()} is a good name.")

#Question #4
#Using GX to represent the name of a food bagel with some  white space:
gx = "  \tbagel\n  "
#Printing GX to display white space:
print(gx)
#printing the Varriable Gx using lstrip, rstrip and strip:
print(gx.lstrip())
print(gx.rstrip())
print(gx.strip())

#Question #5
#Four Operations +, -, * and / to equel 2020 and printing a message:
a = 2019 + 1
print(a)
b = 2021 - 1
print(b)
c = 404 * 5
print(c)
d = int(10100 / 5)
print(d)
#Substituting 2020 in variables a, b, c, and d :
a,b,c,d = 2020, 2020, 2020, 2020
print(a,b,c,d)
#Printing using an f string for varible a and b:
print(f"Adding one to 2019 is equals  {a}")
print(f"Subtracting one from 2021 is equals {b}")
#Printing using a join (+ or,) for varible c and d:
print("Multiplying 404 five times equals" " "+ str(c))
print("Dividing 10100 into five equals" " " + str(d))