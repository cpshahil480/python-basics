def usercheck(f):
    def wrapper(a,b):
        if a=="admin":
            return f(a,b)
        else:
            raise Exception("access error")
    return wrapper

@usercheck
def changepassword(username,newpassword):
    mypassword=newpassword
    return mypassword
print(changepassword("user",65434))