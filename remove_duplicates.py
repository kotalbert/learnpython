# Check if given argument is on the list
def arg_on_list(arg, list):
    
        for i in list:
            if arg == i:
                return True
        else:
            return False


def remove_duplicates(args):
    #First element should be always included
    if len(args) > 0:
        unique_list = []
        unique_list.append(args[0])
        
        for a in args:
            if not arg_on_list(a, unique_list):
                unique_list.append(a)
    else:
        unique_list = []
    return unique_list


#Testing functions:
def list_test(a):
    list = [1,2,3,4]
    print "Argument %d on the list: " %a, arg_on_list(a, list)


list_test(1)
list_test(8)
list_test(2)
list_test(9)
list_test(3)
list_test(10)


def remove_test(args):
    print "Input: ", args, "Output: ", remove_duplicates(args)
    
remove_test([4, 5, 5, 4]) 
remove_test([]) 
