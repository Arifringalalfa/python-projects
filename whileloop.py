i = 1
while i <=6:
    print(i)
    i+=1
i = 2
while i <=100:
    print(i)
    i+=1

i = 0
while i <=100:
    print(i)
    if i == 50:
        break
    i+=1
print("FInished")
i = 0
while i < 6:
    i+=1
    if i ==5 :
        continue
    print(i)

i = 0
while i >6:
    print(i)
    i+=1
else:
    print("i is no longe less than 6")

fruits = ["apple","banana","cherry","orange"]
for x in fruits:
    print(x)

color = ["red","blue","black","green"]
for x in color:
    print(x)

for x in "banana":
    print(x)

color = ["red", "black","blue"]
for x in color:
    print(x)
    if x == "black":
        break

color = ["red", "black","blue"]
for x in color:
    if x == "black":
        continue
    print(x)

for x in range(12):
    print(x)

for x in range(2,30,2):
    print(x)

for x in range(1,30,2):
    print(x)
for x in range(2,50,2):
    print(x)
else:
    print("Finally Finished")

for x in range(30):
    if x == 20:
        break
    print(x)
else:
    print("Finally Finished")

color = ["red","blue","black","orange"]
fruits = ["banana","apple","cherry","banana"]

for x in color:
    for y in fruits:
        print(x,y)    