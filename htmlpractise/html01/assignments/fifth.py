c = int(input("Celsius: "))
def converter(c):
    f = (9/5 * c) + 32
    return f

f = converter(c)
print("Fahrenheit: " + str(f))

