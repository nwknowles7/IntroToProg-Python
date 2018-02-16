objfilename = "//Users/nicoknowles//Desktop//_PythonClass//ToDo.txt"
# Open File and declare variables
fileOpen = open(objfilename, "r")
strData = ""
dicRow = {}
listTable = []

# Use a loop to store data in a dictionary within a list
for line in fileOpen:
    Task, Priority = line.strip().split(",")
    dicRow = {Task: Priority}
    listTable.append(dicRow)
fileOpen.close()

# Display a menu to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Below is your To Do List:")
        print(listTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        addTask = input("Add a task: ")
        addPriority = input("What is the priority for this task? (High/Low)")
        dicRow = {addTask.lower(): addPriority.lower()}
        listTable.append(dicRow)
        print(dicRow, "Added to the To Do List")
        continue

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        removeTask = int(input("Which entry would you like to remove? \n(Type the number of that items position in the list): "))
        listTable.pop(removeTask - 1)
        print("Item Removed")
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        with open(objfilename, 'w') as file_handler:
            for item in listTable:
                file_handler.write("{}\n".format(item))
        fileOpen.close()
        print("Your data has been saved to the To Do List.")
        continue

    elif (strChoice == '5'):
        break  # and Exit the program

