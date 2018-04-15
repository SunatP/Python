has_a = "S" in "S"
has_ahoy = "Sunat" in "Sunat" # use in to look in string or check
print(has_a)    # True
print(has_ahoy) # True

phrase = """   
Python is very hard
"""
length = len(phrase) # use """ to describe long text
a = "Length is "
word = str(length) # str is convert number to string
print(a+ word)   # 24

Name = "Sunat"
Age = 19
print("it's me %s" %Name)
print("I'm %d Years old" % Age)

car = ['Porsche' , 'Toyota' ,'Nissan']
print(car)
car.append('Subaru') # append is add function
print(car)
print(car[2])

animal  = ('snp','chawna','chawbaan')
# animal.__add__(2)
stringf = "tuple cannot edit"
print(stringf)
print(animal)

phone_book = {"Sunat": 832488165 ,"Somchai":12312}
print(phone_book["Sunat"])

if (Age != 19):
    {print("Sawasdee")}
else :{print("error")}

#elif instead else if
for i in range(5): print(i) # count loop by using range
cheese = {2,3,4,5,5,34,4,3}
for a in cheese : print(a)

square = 0
number = 1
print("    ")
while number < 10:
    square = number ** 2 # ** is square or power
    print(square)
    number += 1
    break




