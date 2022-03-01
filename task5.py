from datetime import datetime

try:
    with open('testiv5.txt', 'a') as i :
        i.write('\nAccessed on ' + str(datetime.now()))
    
except:
    print("An exception occurred")