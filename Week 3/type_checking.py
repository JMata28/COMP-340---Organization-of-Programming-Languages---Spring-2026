#Dynamic type checking in Python 

test_var = "Hello"        # allowed
result = 15 * "abc"       # allowed → result is "abc" repeated 15 times
test_result = 14 * 150    # allowed → result is 2100

# But if we try incompatible operations:
x = "Hello" + 5           # ❌ TypeError at runtime

#Difference between implicit variable declaration are dynamic typing
#Implicit variable declaration:
x = 10      # x is created implicitly as an int
y = "hello" # y is created implicitly as a string

#Dynamic typing
x = 10       # x is an int
x = "hello"  # now x is a string — allowed in dynamically typed languages