values = ["Guneet", 10 , "Malhotra", 99.99]
print(values)

# just like strings, we can use both positive and negative indexing here
# also, we can take the subparts too
print(values[0:2])

names = ["abc","def","ghi"]
misc = [names,values]

print(misc)
print(misc[0][2]) # a 2-d list

# append(val) -> appends the value to the last of the list

values.append(100)
print(values)
print(misc) # changes will take place in misc also

# insert(idx,val) -> appends the val at index idx
values.insert(2,500)
values.insert(12,200) # this will insert the value at the end
values.insert(-10,1000) # this will insert the value at the beginning 
print(values)

# remove(val) -> removes the value from the list
values.remove(500)
print(values)

# pop(idx) -> removes the value at index=idx
values.pop(2)
print(values)

#pop() if we don't provide any index, th value at index length-1 will be removed
# this is same as stack LIFO
values.pop()
print(values)

# del-> used to delet multiple values
del values[3:]
print(values)

# extend -> adds multiple values
values.extend([10,20,30,40])
print(values)

# Some inbuilt functions

nums = [9,8,6,3,4,7,2]
print(min(nums))
print(max(nums))
print(sum(nums))

nums.sort()
print(nums)