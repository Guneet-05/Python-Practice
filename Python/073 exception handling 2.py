a = 5
b = 2

try:
    print("resource open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)
    lst = [9,8,6,3]
    print(lst[10]) # other type of error

except ZeroDivisionError as e:
    print("Hey, you cannot divide a number by 0.",e)

except ValueError as e:
    print("Invalid input, please enter an 'INTEGER'")

except Exception as e:
    print("Something went wrong",e)

finally:
    print("resource closed")

print("Bye")