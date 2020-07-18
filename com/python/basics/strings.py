# Working with Text
print("--------------------------------------------------------------------------------------------------------")

# Variable declaration
message = 'Hello World'
print(message)

print("--------------------------------------------------------------------------------------------------------")

# Quotes
message_double_quotes = "Chris's World"
print(message_double_quotes)

message_double_quotes_escape = "This is \"fun\""
print(message_double_quotes_escape)

message_single_quotes_escape = 'Chris\'s World'
print(message_single_quotes_escape)

message_inside_double_quotes = 'This is "fun"'
print(message_inside_double_quotes)

message_with_new_line = """Good Morning! 
Mrs. Williams"""
print(message_with_new_line)

print("--------------------------------------------------------------------------------------------------------")
# Access through index
message = 'Hello World'
print(message[0])
print(message[10])

# slicing
# slicing: starting from index 0 and till index 4, 5 is not inclusive
print(message[0:5])
# slicing: It is same as above
print(message[:5])
# slicing: starting form index 6 through 10
print(message[6:11])
# slicing: It is same as above
print(message[6:])

# Concatenation
greeting = 'Hello'
name = 'Chris'
message = greeting + ', ' + name + '. Welcome!'
print(message)

# formatting: format()
greeting = 'Hello'
name = 'Chris'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# formatting: f string latest feature
greeting = 'Hello'
name = 'Chris'
message = f'{greeting}, {name}. Welcome!'
print(message)

# formatting: f string with code inside placeholder
greeting = 'Hello'
name = 'Chris'
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# len()
message = 'Hello World'
print(len(message))

# upper()
message = 'Hello World'
print(message.upper())

# lower()
message = 'Hello World'
print(message.lower())

# count()
message = 'Hello World'
print(message.count('l'))

# find() and is case-sensitive
message = 'Hello World'
print(message.find('World'))
print(message.find('world'))

# replace() and actual string will not be mutated
message = 'Hello World'
new_message = message.replace('World', 'Universe')
print(message)
print(new_message)

print("--------------------------------------------------------------------------------------------------------")

