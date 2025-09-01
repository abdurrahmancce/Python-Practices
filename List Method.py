fruits = ["apple", "banana"]
print(fruits) # Initial list

print(fruits.index("apple"))
print(fruits.index("banana"))

fruits.insert(1,"orange")
print(fruits) # After inserting orange

fruits.append("grape")
print(fruits) # After appending grape

fruits.extend(["kiwi", "mango"])
print(fruits) # After extending with kiwi and mango

fruits.remove("banana")
print(fruits) # After removing banana

fruits.pop(2)
print(fruits) # After popping element at index 2

fruits.sort()
print(fruits) # After sorting

fruits.reverse()
print(fruits) # After reversing

fruits.clear()
print(fruits) # After clearing the list
