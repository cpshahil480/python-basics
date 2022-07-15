def agecheck(func):
    def wrapper(a,b):
        if b>=18:
            return func(a,b)
        else:
            raise Exception("not eligible")

    return wrapper


@agecheck
def vaccine(name,age):
    return "vaccinated succesfully"
print(vaccine("anu",15))