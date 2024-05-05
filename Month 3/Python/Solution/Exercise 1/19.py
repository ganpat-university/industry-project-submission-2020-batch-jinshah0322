def function(arg1, arg2, kwarg1=None, kwarg2=None, kwarg3=None):
    if kwarg1 is None and kwarg2 is None and kwarg3 is None:
        return arg1 * arg2
    elif kwarg1 is not None and kwarg2 is None and kwarg3 is None:
        return f"{arg1} {arg2} {kwarg1}"
    elif kwarg1 is not None and kwarg2 is not None and kwarg3 is None: 
        return arg1 + arg2 + kwarg1 + kwarg2
    elif kwarg1 is not None and kwarg2 is not None and kwarg3 is not None: 
        result1 = arg1 * arg2
        result2 = kwarg1 * kwarg2 * kwarg3
        return result1 + result2
    else:
        return "Invalid number of arguments"


print(function(7, 11))
print(function(7, 11, kwarg1=4))
print(function(7, 5, kwarg1=7, kwarg2=9))
print(function(7, 3,kwarg1=5, kwarg2=6, kwarg3=7))