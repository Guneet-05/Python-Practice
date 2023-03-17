# everything is object in python
class Computer:
    def config(self):
        print("I5 with 8 GB RAM and 500GB SSD")

comp1 = Computer()
print(type(comp1))
Computer.config(comp1) # way to call config()
comp2 = Computer()
comp2.config() # another way to call config()
# This is mostly used


