a = 5
b = 0

try:
    print("resource opened")
    print(a/b)
    # print("resource closed") this works when there is no exception
except Exception as e:
    # print("resource closed") this works when there is exception
    print("Hey, please don't let the denominator of the division be 0.",e)
finally:
    print("resource closed") # this always works

print("Calculation Successful")