no_of_rows = int (input ("Please enter how many rows you need: "))  
    for i in range (1, no_of_rows + 1):  
        number = 1  
            for j in range (no_of_rows, 0, -1):  
                if j > i:  
                        print (" ", end=' ')  
                    else:  
                        print (number, end=' ')  
                        number += 1  
         print ("")  
