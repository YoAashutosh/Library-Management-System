# importing other files that are used in this function
import Details
import borrow
import Return

# creating a class
class librarymanagementsystem():
    
      """ This class is used to keep the records of books in library.
       Here we have three functions : "Displaying information about Books",
       "Borrowing books" , "Returning Books"   """

      print("                       Welcome to Buddha Library                   ")
      print("<---------------------------------$$--------------------------------->")
    
# using a while loop for creating a condition
      while(True):
            print()
            print("Enter 1 for Display")
            print("Enter 2 for Borrowing a book")
            print("Enter 3 for Returning book")
            print("Enter 4 for Exit")
            print()
            print("<---------------------------------$$--------------------------------->")

# using try to check for exceptions        
            try:
                  user = int(input("Select any of the 4 choices above: 1-4 = "))
                  print()
              
                  if(user == 1):
                        file = open("stock.txt","r")
                        line = file.read()
                        file.close()
                        print("       These are books we have        ")
                        print("<----------------$$------------------>")
                        print(line)
                        print("<----------------$$------------------>")
                  elif(user == 2):
                        Details.details_list()
                        borrow.book_borrow()
                        print()
                  elif(user == 3):
                        Details.details_list()
                        Return.book_return()
                        print()
                  elif(user == 4):
                        print("   Thank you for your visit. Stay safe   ")
                        break
                  else:
                        print("<---------------------------------------->")
                        print(" Please select the choices from above")
                        print("<---------------------------------------->")
            except:# using except to show this message below if try finds an exception
                  print("<-------------------------------------------------->")
                  print("Please enter valid number from above choices")
                  print("<------------------------------------------------->")
            
            
                    
              
    

              
              
        








