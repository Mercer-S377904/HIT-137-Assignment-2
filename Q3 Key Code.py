    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j
    
    counter = 0
    while counter < 5:
        #line 12 to 15 ensures the total is equal to 13
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        #if total is not less than or mare than 13, increase counter (basically checks 3 times to ensure 13)
        else:
            counter += 2


#If lines 12 to 15 force total to equal 13 why not just use total=13 or rather key=13?
