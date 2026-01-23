


# def kids(*kid):
#     print("The youngest child is:"+kid[0])
#     print("The middle child is:"+kid[1])
#     print("The eldest child is"+kid[2])

# kids("Sam","Ken","Robert")


# def arguments(*args):
#     print("The first argument:"+args[0])
#     print("The second argument:"+args[1])
#     print("The third argument:"+args[2])


# arguments("args1","args2","args3")


# def kwarguments(title , *args , **kwargs):
#     print("Title:"+title)
#     print("Individuals:",args)
#     print("Keyword Arguments:",kwargs)

# kwarguments("Identities" , "John Tobias" , "Naveen Andrews" , age=25, city="New York")

# def kwarg(title , *args , **kwargs):
#     print("Title:"+title)
#     print("Individual:",args)
#     print("Information:",kwargs)


# kwarg("Individuals List" , "Jack Daniels" , age = 24 , address = "Chennai")

def arguments(*args):
    print("Argument 1:"+args[0])
    print("Argument 2:"+args[1])
    print("Argument 3:"+args[2])

arguments("Argument 1" , "Argument 2" , "Argument 3")