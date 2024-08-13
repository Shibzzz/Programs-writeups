#create a dictionary to store the names and ages of three people.Print the dictionary
x = {
    "Raju" : 23,
    "Shah" : 21,
    "Ajay" : 25
}
print(x)
 #Access and print the age of a specific person from the dictionary

print(x["Ajay"])

#Add a new person and their age to the dictionary

x.update({"Ram":30})

print(x)

#Modify the age of an existing person in the dictionary

x.update({"Raju":25})

print(x)

# Check if a specific person's name exist as a key in the dictionary

print("Raju" in x.keys())

#create a dictionary and find it's length using len)() function

print(len(x))

# use the keys() to print all the the keys in the dictionary

y=x.keys()

print(y)

# use the value() to print all the values in the dictionary

z=x.values()
print(z)

#use the items() method to print key-value pairs

a=x.items()
print(a)

#Create a dictionary and remove a key-value pairs using pop() method

x.pop("Raju")
print(x)




