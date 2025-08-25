# 1. Function na walang input
def say_hello():
    # Gagawin ng function: mag-print ng "Hello, world!"
    print("Hello, world!")

# Tawagin natin yung function para gumana
say_hello()


# 2. Function na may input (parameter)
def greet(name):
    # 'name' = parang box na tatanggap ng value
    # Magpi-print siya ng greeting gamit yung name
    print("Good morning, " + name + "!")

# Tawagin na may iba't ibang input
greet("Jefferson")
greet("Jay")


# 3. Function na may return (may ibabalik na value)
def add(a, b):
    # 'a' at 'b' = inputs
    # 'return' = ibabalik ang sagot, hindi lang print
    return a + b

# Gamitin yung function at kunin yung sagot
result = add(5, 3)
print("The sum is:", result)
