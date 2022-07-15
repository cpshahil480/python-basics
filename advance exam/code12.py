def valid(f):
    def wrapper(a,b):
        if a=="+911294567890":
            return f(a,b)
        else:
            raise Exception("not valid")
    return wrapper

@valid
def change_number(phn_number):
    new_number=phn_number
    return new_number
print(change_number('+911294567890'))