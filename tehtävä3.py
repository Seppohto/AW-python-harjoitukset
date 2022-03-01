
try:
    file1 = open('testi.txt', 'r')
    count = 0
    
    # Using for loop
    rivit = []
    for line in file1:
        rivit.append(line.strip('\n'))
    
    # Closing files
    rivit.sort()
    rivit.sort(key=len)
    print(rivit)
    file1.close()
except:
    print("An exception occurred")
