age = 24
print("I am {0} years old".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}, {0}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "December"))


print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}"
      .format(28, 30, 31))

print("""Jan: {2}, 
Feb: {0}, 
Mar: {2}, 
Apr: {1}, 
May: {2}, 
Jun: {1}""".format(28, 30, 31))

for i in range(1, 20):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))


# while not ():
    #do something
# while x != ():
    # do something
