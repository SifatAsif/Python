def string_length(star):
    if type(star) == int:
         return "Sorry, integers don't have length"
    elif type(star) == float:
        return "Sorry, floats don't have length"
    else:
        return len(star)
print(string_length(179754.66))




def c_to_f(cel):
    if cel < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=cel*9/5+32
        return f
ce=input("enter:")
print(c_to_f(float(ce)))
