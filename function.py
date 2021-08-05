
cars = ["bmw","ford","ferari","volvo"]
cars.remove("volvo")

print(cars)

cars = ["bmw","ford","ferari","volvo"]
cars.pop()

print(cars)
cars = ["bmw","ford","ferari","volvo"]
cars.append("honda")

print(cars)
cars = ["bmw","ford","ferari","volvo"]
cars.clear()

print(cars)
cars = ["bmw","ford","ferari","volvo"]
cars.clear()

print(cars)


cars = ["bmw","ford","ferari","volvo"]
x=cars.copy()

print(x)
cars = ["bmw","ford","ferari","volvo"]
x=cars.count("ford")

print(x)

fruits = ["apple","banana","Volvo"]
cars = ["volvo","bmw","ford"]
fruits.extend(cars)
print(fruits)

fruits = ["apple","banana","vovlo"]
cars = ["red", "blue", "gren"]

cars.extend(fruits)

print(cars)


fruits = ["red","black","green"]

fruits.reverse()
print(fruits)


fruits = ["red","black","green"]

fruits.sort()
print(fruits)
