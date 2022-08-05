# w3 schools

# if
a = 33
b = 33
if b > a:
  print("b is greater than a") # indentation is important
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

c = 4
d = 3
if c > d: print("c is greater than d") # One line if statement

a = 2
b = 330
print("A") if a > b else print("B") # One line if statement

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
  pass # used to avoid error in empty if statements

a = 50
b = 10
if a > b:
  print("Hello World!")

# while
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break # break loop when statement is true
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #stop current iteration and continue with the next
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# for loops
# list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

#string
for letter in "banana":
  print(letter)

#use of break
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  if fruit == "banana":
    break #stops the loop before it has looped through all items

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break # does not print banana
  print(x)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  if fruit == "banana":
    continue
  print(fruit)

# nested loops
adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjs:
  for fruit in fruits:
    print(adj, fruit)

for x in [0, 1, 2]:
  pass