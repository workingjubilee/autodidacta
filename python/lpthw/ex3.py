#prints text
print("I will now count my chickens:")

#This solves a simple PEMDAS equation. Dividing 30 by 6, then adding 25.
print("Hens", 25.0 + 30 / 6)
#PEMDAS, but this one is a bit confusing. Since % is "divide left operator by right operator, then return remainder" it happens in the MD step of PEMDAS. So 25*3 (75) is then modulus'd (that's apparently its name) by 4, which returns 18 and then a remainder of 3. That 3 is then subtracted from 100, giving 97.
print("Roosters", 100.0-25*3%4)
#prints text
print("Now I will count the eggs:")

#PEMDAS, see above note on line 5 about how modulus works. It's a division-but-return-remainder step.
print(3.0 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 -7?")
#This outputs True or False based on whether the inequality (3+2 is less than 5-7) is correct.
print(3.0+2<5-7)# In this case, it's False.

#Displays text, then solves a PEMDAS equation and displays the value after the text.
print("What is 3 + 2?", 3.0 + 2)
#Displays text, then solves a PEMDAS equation and displays the value after the text.
print("What is 5 - 7?", 5.0 - 7)

#prints text
print("Oh, that's why it's False.")
#prints text
print("How about some more.")

#prints text and then outputs a true/false based on whether the inequality is true or false.
print("Is it greater?", 5.0 > -2)
#prints text and then outputs a true/false based on whether the inequality is true or false. >= is "greater than or equal to". This will error if there is a space between the symbols.
print("Is it greater or equal?", 5.0 >= -2)
#prints text and then outputs a true/false based on whether the inequality is true or false. <= is "less than than or equal to". This will error if there is a space between the symbols.
print("Is it less or equal?", 5.0 <= -2)
