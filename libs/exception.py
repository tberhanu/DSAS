
class MyCustomException(Exception):
    pass
###########################################################

class AnotherCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)       
        self.message = message  
###########################################################

try:
    # operation
    print("do something")
except ZeroDivisionError as e:
    # handle zero division error
    pass
except MyCustomException as e:
    # handle custom error
    pass
except Exception as e:
    # handle exception
    pass
else:
    print("No exceptions were raised.") # executes if no exception was raised in the try block

finally:
    print("This will always execute.") # executes regardless of whether an exception was raised or not


###########################################################
try:
    # operation
    if some_other_condition:
        raise AnotherCustomException("This is another custom exception")
except AnotherCustomException as e:
    print(e.message)
    print("do something")

###########################################################
try:
    print("do something")
except Exception:
    print("Something went wrong")
    raise   # let the caller handle it (throws the original exception up the call stack)

###########################################################
some_condition = True
if some_condition:
    raise Exception("This is an exception")
###########################################################
if some_condition:
    raise MyCustomException("This is a custom exception")
