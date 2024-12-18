var_global="Good Morning"
def outer_body():
    var_outer="Good Afternoon"
    def inner_body():
        var_inner="Good Evening"
        print("Variable Global from inner function:",var_global)
        print("Variable Outer from inner function:",var_outer)
        print("Variable Inner from inner function:",var_inner)
    inner_body() 
    print("Variable Global from Outer function:",var_global)
    print("Variable Outer from Outer function:",var_outer)
   # print("Variable Inner from Outer function:",var_inner)
print("Variable Global from Main function:",var_global)
#print("Variable Outer from Main function:",var_outer)
#print("Variable Inner from Main function:",var_inner)
outer_body()
print("Good Night..")
