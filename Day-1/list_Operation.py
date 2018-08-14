l = [1, 2, 3.14, 'data']
print(type(l))
l.append([3, 4]) # add one element of list
print(l)
l.extend(['delta', 5, 6]) # add a list
print(l)
l.insert(3, 'beta') # insert before index 3
print(l)
l.remove('data') # delete an element
print(l)