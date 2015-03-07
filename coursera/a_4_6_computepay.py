"""
Programming for Everybody (Python)
Assignment 4.6

Calculate total pay.
"""

def computepay(h,r):
    
    try:
        h_f = float(h)
        r_f = float(r)
    except:
        print "Enter a valid number."
        quit()
    
    standard_hours_count = 40
    overtime_bonus = 1.5
    
    pay = 0.0
    
    overtime = h_f - standard_hours_count
    
    if overtime > 0:
        pay = standard_hours_count * r_f + overtime*r_f*overtime_bonus
    else:
        pay = h_f * r_f
    
    return pay

hrs = raw_input("Enter Hours:")
rt = raw_input("Enter Rate:")
p = computepay(hrs,rt)
print "Pay",p