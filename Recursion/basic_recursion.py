count = 0
def recursion_function():
    global count
    #Base condition(Ending condition)
    if count == 3:
        return
    print(count)
    count += 1
    recursion_function()#function call itself

print(recursion_function())


    