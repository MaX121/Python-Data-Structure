# user input on searching target
target = input("Searching name :: ");

# define list and dictionary
name = grade = rank = []
dictionary = {'name':[], 'grade':[], 'rank':[]}

# user input to add the value to the dictionary
for num in range (0,2) :
    name.append(input("Your Name :: "))
    grade.append(input("Your Grade :: "))
    rank.append(input("Your Rank :: "))
    print("\n")

# append the value from list and add it into dictionary
dictionary['name'].append(name)
dictionary['grade'].append(grade)
dictionary['rank'].append(rank)

# searching from desired value and display it details as a stdout
for num in range (len(name)) :
    if (name[num].lower() == target.lower()) :
        print(dictionary.__getitem__('name')[0][num])
        print(dictionary.__getitem__('grade')[0][num])
        print(dictionary.__getitem__('rank')[0][num])
        break
    else :
        print("Data Doesn't Exist")

# deleting data from desired value and display the report
for num in range (len(name)) :
    if (name[num].lower() == target.lower()) :
        del dictionary.__getitem__('name')[0][num]
        del dictionary.__getitem__('grade')[0][num]
        del dictionary.__getitem__('rank')[0][num]
        print("Data successfully deleted")
        break
    else :
        print("Data Doesn't Exist")

# update data from desired value and display the data as stdout
for num in range (len(name)) :
    if (name[num].lower() == target.lower()) :
        dictionary.__getitem__('name')[0][num] = "Hello"
        dictionary.__getitem__('grade')[0][num] = "C"
        dictionary.__getitem__('rank')[0][num] = "333"
        print("Data successfully changed")
    else :
        print("Data Doesn't Exist")