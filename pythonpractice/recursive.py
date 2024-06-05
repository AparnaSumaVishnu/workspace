#f=n*(n-1)*...1
def fact(n):
    print(f"Current n value is:{n}")
    if n==1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(9))    