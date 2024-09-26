# Define the first function

print("func1() is missing")
print("this is new line")

print("this is extra text")

# Define another function that calls fun1
def fun2():
    print("Calling fun1 from fun2...")
    fun1()  # Call fun1 inside fun2gt
    print("fun1 has been called!")

# Call fun2 to execute the functions
fun2()
