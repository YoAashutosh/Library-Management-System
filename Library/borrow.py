# importing other files for using their methods in this function
import Details
import date_time

# creating a function for borrowing book 
def book_borrow():
    borrowed = False # assigning false value to borrowed variable
    # using while for creating a loop 
    while(True):
        first_name = input("Enter the first name for borrowing: ")
        if first_name.isalpha(): # checks if the typed letters are characters or not
            break
        print("<------------------$$------------------->")
        print("Please input valid characters from A to Z")

     # using while for creating a loop 
    while(True):
        last_name = input("Enter the last name for borrowing: ")
        if last_name.isalpha():# checks if the typed letters are characters or not
            break
        print("<------------------$$------------------->")
        print("Please input valid characters from A to Z")

    # creating a variable for storing the information about borrower
    borrowed_by = "Borrowed by-"+first_name+".txt"

    # opening the object created above to store file
    with open(borrowed_by,"w") as obj: # Here "w" is used for writing in file
        obj.write("\t                 Buddha Library                   "+"\n")
        obj.write("\t        Borrower name is: "+first_name+" "+last_name+"\n")
        obj.write("\t    Date: " +date_time.getDate()+"\t   Time:"+date_time.getTime()+"\n\n")
        obj.write("S.N. \t\t Name of the Book \t\t   AuthorName  \n")
    
    while borrowed == False:
        print()
        print("--------------------------Please select the book which you want to borrow-------------------------- ")
        for i in range(len(Details.nameofbook)):
            print("Enter",i,"to borrow book", Details.nameofbook[i])
            
        # using try for searching an exception
        try:
            print("<--------------------------------------------------->")
            num = int(input("Enter the respective number of books  you want to buy: "))
            if(num < 0):     
                print("<--------------------------------------------------->")
                print("Please input positive value")
                print("<--------------------------------------------------->")
                
            else:
                print("<--------------------------------------------------->")
                # using try for searching an exception
                try:
                    if(int(Details.quantityofbook[num]) > 0):
                        print("The book is available")
                        print("<--------------------------------------------------->")
                    # opening the object created above to store file
                        with open(borrowed_by,"a") as obj:# Here "a" means append into the object used
                            obj.write("1.\t\t"+Details.nameofbook[num]+"\t\t "+Details.nameofauthor[num]+"\n")

                        Details.quantityofbook[num] = int(Details.quantityofbook[num]) - 1
                        with open("stock.txt","w") as obj:
                            for i in range(len(Details.lines)):
                                obj.write(Details.nameofbook[i] + "," + Details.nameofauthor[i] + "," + str(Details.quantityofbook[i]) + "," + "$" + Details.cost[i] + "\n") 

                        # for borrowing multiple books
                        # creating a loop
                        loop = True
                        count = 1
                        # creating a while loop and assigning it true for infinite use
                        while loop == True:
                            more_book = str(input("Wanna borrow more? Sorry, but you can't borrow same book twice. Press y for Yes and n for No.: "))
                            #Here ".upper" checks if the input value is upper case or not
                            if(more_book.upper() == "Y"):
                                count = count + 1 
                                print("<--------------------------------------------------->")
                                print("Please select an option below for buying again:")
                                print("<--------------------------------------------------->")

                                for i in range(len(Details.nameofbook)):
                                    print("Enter", i, "to borrow book", Details.nameofbook[i])
                                print("<--------------------------------------------------->")
                                num = int(input("Enter the respective number of books  you want to buy: "))
                                print("<--------------------------------------------------->")
                            

                                if(int(Details.quantityofbook[num]) > 0):
                                    print(" The book is available")
                                    print("<--------------------------------------------------->")
                                    with open(borrowed_by,"a") as obj:
                                        obj.write(str(count) +"\t\t"+Details.nameofbook[num]+"\t\t "+Details.nameofauthor[num]+"\n")

                                    Details.quantityofbook[num] = int(Details.quantityofbook[num]) - 1
                                    with open("stock.txt","w") as obj:
                                        for i in range(len(Details.lines)):
                                            obj.write(Details.nameofbook[i]+","+Details.nameofauthor[i]+","+str(Details.quantityofbook[i])+","+"$"+Details.cost[i]+"\n")
                                            borrowed=False
                                else:
                                    loop=False
                                    break
                            elif (more_book.upper() == "N"):
                                print("<--------------------------------------------------->")
                                print("<--------------------------------------------------->")
                                print ("         Thank you for using our service.              ")
                                print("<--------------------------------------------------->")
                                print("<--------------------------------------------------->")
                                loop = False
                                borrowed = True                   
                            else: 
                                print("Please choose as instructed")
                        
                    else:
                        print("The book isn't currently available")
                        book_borrow()
                        borrowed = False
                # throws the message if try catches an exception
                except IndexError:
                    print("")
                    print("Please choose book according to their number.")
            
                
        # throws the message if try catches an exception
        except ValueError:
            print("")
            print("Please choose as suggested.")
