# importing other files for using their methods in this function
import Details
import date_time 

# creating a function for returning book 
def book_return():
    print("<--------------------------------------------------->")
    name = input("Enter name of borrower: ")
    print("<--------------------------------------------------->")

    # creating a variable for storing the information about borrower
    borrowed_by = "Borrowed by-"+name+".txt"
    # using try for searching an exception
    try:
        # opening the object created above to store file
        with open(borrowed_by,"r") as file: # Here "r" means read the object used
            line = file.readlines() # created a list named line and stores file
            line = [borrowed_by.strip("$")for borrowed_by in line]
        
        with open(borrowed_by,"r") as file:
            read_ = file.read() # reads the file
            print(read_)
    # throws the message if try catches an exception
    except:
        print("Please recheck the borrower's name")
        book_return()

    # creating a variable for storing the information about return
    borrow_returned ="Returned by-"+name+".txt"
   # Here "w" is used for writing in file
    with open(borrow_returned,"w") as file:
        file.write("                Buddha Library "  +    " \n")
        file.write("                Returned By: "+ name+"\n")
        file.write("\t\t\t\t   Date: " + date_time.getDate()+" \t\t\t\t    Time:"+ date_time.getTime()+"\n\n")
        file.write("S.N.\t\tName of the book\t\tCost\n")


    charge = 0.0         
    for i in range(len(Details.lines)):
        if Details.nameofbook[i] in read_:
            with open(borrow_returned,"a") as file:
                file.write(str(i+1)+"\t\t"+Details.nameofbook[i]+"\t\t$"+Details.cost[i]+"\n")
                Details.quantityofbook[i] = int(Details.quantityofbook[i])+1
            charge += float(Details.cost[i])
            
    print("\t\t\t\t\t\t " + "<------------------->")
    print("\t\t\t\t\t\t " + "   Total Cost: "+"$"+str(charge))
    print("\t\t\t\t\t\t " + "<------------------->")
    print("<--------------------------------------------------->")
    print("Check if the book return date is expired")
    print("<--------------------------------------------------->")
    status = input("Press y for Yes and n for No: ")
    print("<--------------------------------------------------->")
    #Here ".upper" checks if the input value is upper case or not
    if(status.upper() == "Y"):
        print("By how many days was the book returned late?")
        days = int(input()) # Taking input for expiry days from user
        fine = 3*days
        with open(borrow_returned,"a") as file:# Here "a" means append into the object used
            file.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        charge = charge + fine
    

   # printing final total
    print("Final Total: "+ "$"+str(charge))
    print("<--------------------------------------------------->")
    with open(borrow_returned,"a") as file:
        file.write("\t\t\t\t\tTotal Charge: $"+ str(charge))
    
    # opening stock.txt file     
    with open("stock.txt","w") as file:
            for i in range(len(Details.lines)):
                file.write(Details.nameofbook[i]+","+Details.nameofauthor[i]+","+str(Details.quantityofbook[i])+","+"$"+Details.cost[i]+"\n")

    
