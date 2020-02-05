
try:
    age = int(input("What is your age? "))
except NameError:
    print("Error: You Must Enter a Number for your age")
except SyntaxError:
    print("Error: You Must Enter a Number for your age")
else:
    print "Your age is " + str(age)
    retire = str(65-age)
    print "Years left until retirement:" , retire, "years"
