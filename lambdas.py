languages = ["HTML", "JavaScript", "Python", "Ruby"]
# print filter(lambda x: x == "Python", languages)

squares = [x**2 for x in range(1,11)]
l = lambda x: x >= 30 and x<=70
# print filter(l, squares)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
l = lambda x: x != 'X'
message = filter(l, garbled)
print message