allData = [] #all informatioin will be stored here(nested list)

#Options available to choose which action
def mainMenu():
    print("\n***** Maria's sari-sari store *****\n__________________________________")

    while True: #to loop the options showing up, until the user chooses exit
        print("\n1.Add item\n2.View invoice\n3.Delete all data\n4.Exit")
        userInput = input("Enter your choice(1-3): ")

        #prompt item info, append all info to the main list(allData)
        if userInput == "1":
            try:
                itemName = input("\nEnter item name: ").capitalize() #To have uniform item name format (capitalized)
                quantity = int(input("Enter item quantity: "))
                price = float(input("Enter item price: "))
                subTotal = float(quantity * price)
                allData.append([itemName,quantity,price,subTotal]) #add to the main list
                print(f"Item: ({itemName}), were added successfully!")
            except ValueError:
                print(">>>>Try again!, you must input numbers only.")

        #if user want to display the organized data/receipt
        elif userInput == "2":
            #checks if there is already data in the list
            if allData:
                displayInfo()
            else:
                print("\n>>>>No data found, add an item first!!!!")
        #if user want to delete all data
        elif userInput == "3":
            while True:
                confirm = input("\nAre you sure you want to delete all the data?(Y or N): ")
                if confirm.lower() == "y":
                    #To remove all the content of the allData list, using for loop and pop()
                    for i in range(len(allData)-1,-1,-1):
                        allData.pop(i)
                    print("\n>>>>All data were deleted!")
                    break
                elif confirm.lower() == "n":
                    break
                else:
                    print("\n>>>>Invalid input!")
            
        #if user want to exit
        elif userInput == "4":
            print(">>>>Exiting the program....")
            break

        #for invalid input
        else:   
            print(">>>>Invalid Input!")

#function to display the receipt
def displayInfo():

    print("\n*******************************************************")
    print(f"{'Item Name':<15}{'|Quatity':<14}{'|Price':<14}{'|Subtotal':<14}") #to have specific spacing
    #iterate through the allData list to access each info for each group of items
    for info in allData:
        #to match the label spacing,formating with (,) for thousands plus and 2 decimal
        print(f"{info[0]:<15}|{info[1]:<13}|{info[2]:<13,.2f}|{info[3]:<13,.2f}") 

    #calculate the totalCost/total of all items
    totalCost = 0
    for info in allData:
        totalCost += info[3]

    print("___________________________________________")
    print(f"TOTAL COST = ₱{totalCost:,.2f}") #to add (,) for 1k plus and 2 decimals
    print("*******************************************************")

mainMenu() #call the func to start the program