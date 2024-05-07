# Starting out building in Python
# Creating two variables that will take user inputs as integers
x = 5
y = 25
print(x)
print(y)

# Using python f string
name = "Olivia"
house_number = 41
print(f"I am {name} and I live in house {house_number}.")

# This allows you to print these two numbers and it shows these two numbers
a = int(input("Enter a number"))
b = int(input("Enter a number"))
print(x)
print(y)

# Now print the sum of both numbers entered 
d = int(input("Enter a number"))
t = int(input("Enter a number"))
print("The sum of", d, "and", t, "is:", d + t)

# multiplying the numbers inputed
o = int(input("Enter the first number: "))
p = int(input("Enter the second number: "))
print("The product of", o, "and", p, "is:", o * p)


#now divide the numbers
n = int(input("Enter a number"))
m = int(input("Enter a number"))
print("The result of the division is:", m / n)

# Square root of the numbers entered
c = int(input("Enter a number"))
f = int(input("Enter a number "))
print("The square root of", o, "and", f, "is:", c ** f)


# Writing a function that takes two numbers and returns the sum of both (division,multiplication and square root)
def sum_t_u(t, u):
    return t + u

result = sum_t_u(200, 300)
print(result)


def divide_v_w(v, w):
    return v / w


result = divide_v_w(1000, 200)
print(result)


def multiply_g_h(g, h):
    return g * h


result = multiply_g_h(9, 41)
print(result)


def square_root_j_k(j, k):
    return j ** k


result = square_root_j_k(10, 10)
print(result)

