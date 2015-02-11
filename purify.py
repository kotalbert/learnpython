def purify(args):
    result = []
    
    for a in args:
        if a%2==0:
            result.append(a)
    return result
    
#Testing program
print purify([1,2,3])