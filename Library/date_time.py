# using getDate() function
def getDate():
    # importing datetime
    import datetime
    now = datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date()) 

# using getTime() function
def getTime():
    # importing datetime
    import datetime
    now = datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())
