from datetime import datetime, timedelta
from threading import Timer
from threading import Thread
import one,two,three,four,source_data_generator,final_data_generator
import pytz
import os, time


#Time zone
tz = pytz.timezone('US/Eastern')
my_date = datetime.now(tz).replace(tzinfo=None)


print("\n\nTodays Date is:")
print(my_date,"\n\n")

#Time settling
user_hour=17
user_minute=0
pass_time=timedelta(days=1)


def Begin():
    
    my_date = datetime.now(tz).replace(tzinfo=None)
    x=my_date
    #Defines how many second will wait
    y = x.replace(day=x.day, hour=user_hour, minute=user_minute, second=0, microsecond=0)+ pass_time
    delta_t=y-x
    print(delta_t)

    secs=delta_t.total_seconds()
    print(secs)
    ##Waiting day time
    t = Timer(secs, Begin)
    t.start()
    
    
    #My code
    ##
    ##
    
    #Threads one,two,three and four
    threads=[Thread(target=one.run),Thread(target=two.run),Thread(target=three.run),Thread(target=four.run)]

    for thread in threads:
        Thread.start(thread)
    
    #Wait until one two three and four finish
    for x in threads:
        x.join()
        
    #Start source_data_generator
    source_data=Thread(target=source_data_generator.run)
    Thread.start(source_data)
    source_data.join()
    
    #Start final_data_generator
    final_data=Thread(target=final_data_generator.run)
    Thread.start(final_data)
    final_data.join()


    ##
    ##
    print("\n*******************\n",my_date,"\nTodays Process Has Finished\nWaiting For Next Day\n*******************")
    

if __name__ == "__main__":
    
    my_date = datetime.now(tz).replace(tzinfo=None)

    x=my_date
    print(x)
    #Defines first start date
    y = x.replace(day=x.day, hour=user_hour, minute=user_minute, second=0, microsecond=0)
    delta_t=y-my_date
    print(y)
    print(x)
    secs=delta_t.total_seconds()
    print(secs)
    ##Waiting first day time and then wait for next day
    t = Timer(secs, Begin)
    t.start()
    