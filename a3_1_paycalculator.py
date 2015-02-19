hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)

standard_hours_count = 40
overtime_bonus = 1.5

pay = 0

overtime = h - standard_hours_count

if overtime > 0:
    pay = standard_hours_count * r + overtime*r*overtime_bonus
else:
    pay = h * r
    
print pay