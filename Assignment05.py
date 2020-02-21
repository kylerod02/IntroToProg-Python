# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# KRodriguez,2/18/2020,Created started script
# KRodriguez,2/19/2020,Added code to complete assignment 5
# KRodriguez,2/20/2020,Rewrote program to use more functions specifically to read and write to file
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
txtFile = "ToDoList.txt"# File name
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """   # A menu of user options
strChoice = "" # A Capture the user option selection
lstTable = []  # Instantiating lstTable


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# TODO: Add Code Here
def read_file(txtFile):
    objFile = open(txtFile, 'r')
    for row in objFile:  # looping through the file and making each row a list and appending the lists to tblList
        i, v = row.split(',')
        lstRow = [i, v.strip()]  # strip function used to remove \n which was causing bugs on program reruns by
        lstTable.append(lstRow)  # adding empty lines and failing on line 37 due to nothing to split
    # print(lstTable)  # used to keep track of current lstTable when starting program
    return lstTable


# User choice 1
# Function shows the current changes to the data loaded from the file by looping through the lstTable
# and printing out Dict's. The strip function is used to remove new line characters from the print
def current_data(lstTable):
    for row in lstTable:
        dicRow = {'Task': row[0].strip(), 'Priority': row[1].strip()}
        print(dicRow)

# User choice 2
# Function prompts the user to enter a new task and priority level and appends the row to the current lstTable
def add_task(lstTable):
    strTask = input('Enter a Task: ')
    strPrio = input('Enter a Priority Level e.g. (Low, Med, High): ')
    row = [strTask.strip(), strPrio.strip()]
    lstTable.append(row)
    # print(lstTable) # used to debug during runs with carriage returns

# User choice 3
# Function depicts the current tasks that can be removed and lets user know of failures from incorrect inputs
# before returning to menu
def rem_task(lstTable):
    status = 'row not found'

    for row in lstTable:
        print(row[0])
    print()
    strItem = input('Above task to remove: ')

    for row in lstTable:
        if row[0].lower() == strItem.lower():
            lstTable.remove(row)
            status = 'Row removed'
    print(status)

# User choice 4
# Function opens the txt file in write mode and writes the lstTable to it line by line
def save_data(txtFile, lstTable):
    objFile = open(txtFile, 'w')
    for row in lstTable:
        objFile.write(row[0] + ',' + row[1] + '\n')
    objFile.close()

lstTable = read_file(txtFile)  #initial reading of file and creation of data in memory

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        current_data(lstTable)
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        add_task(lstTable)
        continue

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        rem_task(lstTable)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        save_data(txtFile, lstTable)
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program