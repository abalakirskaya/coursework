from stack import Stack

example = Stack()
print('Testing a Stack ADT...')
example.push('now.')
example.push('ADT ')
example.push('Stack ')
example.push('a ')
example.push('testing ')
example.push('are ')
example.push('We ')
assert example.is_empty() == False
assert example.pop() == 'We '
assert example.pop() == 'are '
assert example.is_empty() == False
while example.is_empty() is False:
    example.pop()
assert example.is_empty() == True
print('It`s OK!')
