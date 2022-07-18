# creating a function for details about books 
def details_list():
    # declaring global variables for using them out of this file
    global nameofbook
    global nameofauthor
    global quantityofbook
    global cost
    global lines
    #creating empty lists
    nameofbook = []
    nameofauthor = []
    quantityofbook = []
    cost = []
    # opening file stock.txt
    file = open("stock.txt","r")
    lines = file.readlines() # creates a list named lines
    lines = [x.strip('\n') for x in lines] # creates a list inside list

    # using for loop to get access in list(lines)
    for i in range(len(lines)):
        let_index = 0 # assigning value 0
        # Here ".split(',')" splits the list from that comma(,)
        for a in lines[i].split(','):
            if(let_index == 0):
                nameofbook.append(a)
            elif(let_index == 1):
                nameofauthor.append(a)
            elif(let_index == 2):
                quantityofbook.append(a)
            elif(let_index == 3):
                cost.append(a.strip("$"))
            let_index += 1
                
    

    



    
    
