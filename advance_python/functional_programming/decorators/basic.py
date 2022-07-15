def changevalue(func):
    def wrapper(a,b):
        if a>=b:
            return func(a,b)

        else:
            a,b=b,a
            return func(a,b)

    return wrapper

@changevalue
def sub(n1,n2):
    return n1-n2
# print(sub(2,4))

@changevalue
def div(n1,n2):
    return n1/n2
print(div(2,4))



