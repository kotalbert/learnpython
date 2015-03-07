"""
Programming for Everybody (Python)
Assignment 5.2

Input a series of numbers until "done" string is encountered.
Print maximum and minimum of entered numbers.
"""

largest = None
smallest = None
while True:
        txt = raw_input("Enter a number: ")
        if txt == "done" : break
    
        try: num = int(txt)
        except: 
            print "Invalid input"
            continue
        
        if largest is None:
            largest = num
        
        if smallest is None:
            smallest = num
            
        if smallest > num: smallest = num
        if largest < num: largest = num 
    
print "Maximum is", largest
print "Minimum is", smallest