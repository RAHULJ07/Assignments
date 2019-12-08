for row in range(0,5):
    for column in range(row+1):
        print('*', end =" ")
    print('\r')
    
for row in range(5,0,-1):
    for column in range(row-1):
        print('*', end =" ")
    print('\r')
