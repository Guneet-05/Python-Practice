nums = [9,8,6,3,4,7,2]

it = iter(nums)
print(it) # prints the iterator object
print(it.__next__())
print(next(it))

# list, tuple, etc are iterable objects that give an iterator when passed
# as a parameter to the iter(iterable) method

class TopTen:

    def __init__(self) -> None:
        self.counter = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if self.counter<=10:
            val = self.counter
            self.counter +=1
            return val
        else:
            raise StopIteration

values = TopTen()
for i in values:
    print(i)