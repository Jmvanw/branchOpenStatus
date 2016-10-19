from datetime import datetime
from pytz import timezone

#Portland's time is Local time.
now_portland = datetime.now()

#Portland
print ("Portland, Oregon's time:")
print now_portland.strftime('%Y/%m/%d %H:%M:%S')
if ("09:00:00") < now_portland.strftime("%H:%M:$S") and now_portland.strftime("%H:%M:$S") < ("21:00:00"): 
    print ("Status: Open")
else:
    print ("Status: Closed")

#New York City
print ("\nNew York City, New York's time:")
now_newYork = datetime.now(timezone('America/New_York'))
print now_newYork.strftime("%Y-%m-%d %H:%M:%S %Z%z")
if ("09:00:00") < now_newYork.strftime("%H:%M:$S") and now_newYork.strftime("%H:%M:$S") < ("21:00:00"): 
    print ("Status: Open")
else:
    print ("Status: Closed")

#London    
print ("\nLondon, England's time:")
now_london = datetime.now(timezone('Europe/London'))
print now_london.strftime("%Y-%m-%d %H:%M:%S %Z%z")
if ("09:00:00") < now_london.strftime("%H:%M:$S") and now_london.strftime("%H:%M:$S") < ("21:00:00"): 
    print ("Status: Open")
else:
    print ("Status: Closed")
