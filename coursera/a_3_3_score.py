"""
Programming for Everybody (Python)
Assignment 3.3

Calculate grade based on score input.
"""

inp = raw_input("Enter score between 0.0 and 1.0:")
try:
    score = float(inp)
except:
    print "Enter valid number."
    quit()
    
if score > 1.0 or score < 0.0:
    print "Enter number between 0.0 and 1.0"    
    quit()

if score >= 0.9: grade = 'A'
elif score >= 0.8: grade = 'B'
elif score >= 0.7: grade = 'C'
elif score >= 0.6: grade = 'D'
else: grade = 'F'
    
print grade    