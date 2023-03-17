# Assumption here is that we cannot modify the div function body
# say we have imported it from some library
# and we want to make it smart so that it automatically
# always keeps the numerator above denominator

def div(a,b):
    return a/b

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    
    return inner

div = smart_div(div)
print(div(2,4))