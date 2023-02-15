numbers=[10,20,30,40]
numbers[2]=9
print (numbers)
cars=["brand","porsho","jeep"]
cars.append("toyota")
print(cars)
cars.remove("brand")
print(cars)

numbers=[23, 76, 55, 55, 34]
numbers.pop(2)
print(numbers)

numbers=[3,4,5,7,9]
length=len(numbers)
print(length)
length=numbers.count(5)
print(length)

numbers.reverse()
print(numbers)


for i in numbers:
     print(i)
for i in range(3):
  print(numbers[i])
     