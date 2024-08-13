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
