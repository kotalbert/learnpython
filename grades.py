grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(scores):
    total = 0
    for s in scores:
        total += s
    return total
    
def grades_average(grades):
    return grades_sum(grades)/float(len(grades))
    
def grades_variance(scores):
    variance = 0
    average = grades_average(scores)
    
    for s in scores:
        variance += (average - s) ** 2
        
    return variance/float(len(scores))

def grades_std_deviation(variance):
    return variance ** 0.5

# Printing   
print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(grades_variance(grades))