my_dict = {
    "Arwena": "Dominant",
    "Albert": "Wspanialy",
    "Ursjusz": "Rudy"
}

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
even_squares = [x**2 for x in range(1,11) if x%2 == 0]

cubes_by_four = [x**3 for x in range(1,11) if (x**3)%4==0]

# List slicing
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10

# Omitting Indices
# print my_list[::2]

# Reversing a List
backwards = my_list[::-1]

# Stride  Lenght
to_one_hundred = range(101)

backwards_by_tens = to_one_hundred[::-10]
# print  backwards_by_tens

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

# print movies.items()

threes_and_fives = [x for x in range(1,16) if x%3==0 or x%5==0]
# print threes_and_fives

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]

#Printing...
# print my_dict.items()
# print my_dict.keys()
# print my_dict.values()

# for key in my_dict:
#     print key, my_dict[key]

# print even_squares
# print cubes_by_four