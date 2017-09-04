from datetime import datetime
from pytz import timezone

def checkOpenClose(branchTime):
    if ("09:00:00") < branchTime.strftime("%H:%M:%S") and branchTime.strftime("%H:%M:%S") < ("21:00:00"): 
        print ("Status: Open")
    else:
        print ("Status: Closed")



def main():    
    #Portland's time is Local time.
    now_portland = datetime.now(timezone('US/Pacific'))

    #Portland
    print ("Portland, Oregon's time:")
    print (now_portland.strftime('%Y/%m/%d %H:%M:%S'))
    checkOpenClose(now_portland)

    #New York City
    print ("\nNew York City, New York's time:")
    now_newYork = datetime.now(timezone('America/New_York'))
    print (now_newYork.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    checkOpenClose(now_newYork)

    #London    
    print ("\nLondon, England's time:")
    now_london = datetime.now(timezone('Europe/London'))
    print (now_london.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    checkOpenClose(now_london)

if __name__=='__main__':
    main()
