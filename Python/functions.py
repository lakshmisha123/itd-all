


# counter = 10

# def someFunc():
#     global counter
#     counter = 100
#     return counter, 100

# a, b, c = someFunc()



# lst1 = ["ok", "2", "3", "ZZZ"]



# print(lst1.sort())

# def some():
    
#     return 



# def sum(a, b, c, d=200):
#     return {
#         "first":a,
#         "second":b,
#         "thrird":c,
#         "fourth":d,
#     }


# out1 = sum(10, 20, 30, "ABC")

# print(out1)


# def printDetails(name, age, city):
#     print(f"Hi my name is {name}, I am {age} years old and from {city}.")



# printDetails(city="Bangalore", age=20, name="Sachin")


# def sumAll(*nums):
#     print(type(nums))
#     sum = 0
#     for el in nums:
#         sum += el
#     return sum



# print(sumAll(10, 20, 1, 40, 50, 60))


# def printDetails(**kw):
#     print(type(kw))
#     print(kw.keys())
#     print(kw.values())


# printDetails(name="ok", age=20)



# printDetails(school="ok", score=20)


# def sumAll(*nums, num1):
#     print(nums)
#     print(num1)

# sumAll(20, 30, num1=2)




# def printDetails(name, city, country='INDIA'):
#     print(name, city, country)


# printDetails("Sachin", "Banglore")


# def wrapper_function():
#     x = 10
#     def innerFunction():
#         print(x)

#     def innerFunction2():
#         print(x)

#     innerFunction()

# inner = wrapper_function()
# inner()



#Closure
# def someFunction(num1):

#     def innerFunction(num2):
#         return num2 ** num1
    

#     return innerFunction


# square = someFunction(2)
# cube   = someFunction(3)




# output = square(16)
# print(output)



# output = square(5)
# print(output)



# output = square(15)
# print(output)


# print(cube(3))


# print(someFunction(2)(3))

# a = someFunction(2)
# a(3)

# import time


# def calc_time_exec(func):
#     def wrapper(*args, **kwags):
#         start_time = time.time()
#         func(*args, **kwags)
#         end_time = time.time()
#         print(f"Total time for execution is ==> {end_time-start_time}")
#     return wrapper


# # @login
# # def greet(num):
# #     print("Good Day!!")

# @calc_time_exec
# def delay(num, num2):
#     time.sleep(10)
#     print("Good Day!!")
#     print(num + num2)



# # out = calc_time_exec(delay)

# # out(num, num2)

# # greet()

# delay(100, 1)

# lst1 = [10, 20, 30]

# def doSomething(inp):
#     some_var = inp.copy()
#     some_var.append(200)
#     inp.clear()

#     return some_var

# lst2 = lst1
# out = doSomething(lst2)






# square = lambda x : x * x

# print(square(5))


# add  = lambda a, b : a + b

# print(add(10, 20))


# def wrapper(num1):
#     return lambda num2: num2 ** num1


# square = wrapper(2)

# out = square(13)

# print(out)


# func1 = lambda arg: arg ** 2



# def func1 (arg):
#     return arg ** 2