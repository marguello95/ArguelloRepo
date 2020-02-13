import sys

#Creates name as empy and will then fill with input from .bat file
#Will allow for 3 names to be input into the .bat file
name = []
name.append(sys.argv[1])
name.append(sys.argv[2])
name.append(sys.argv[3])

#Prints out number of letters of each name, as well as the name that was input
for x in name:
    print("There are " + str(len(x)) + " letters in the name " + str(x))
