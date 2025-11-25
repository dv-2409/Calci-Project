"""
Simple Calculator CLI
Used for Git merge conflict demonstration.
"""

def add(a, b):

    return a + b



def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def main():
    print("Simple Calculator")
    a = 10
    b = 5
    print("add:", add(a,b))
    print("sub:", sub(a,b))
    print("mul:", mul(a,b))
    print("div:", div(a,b))

if __name__ == "__main__":
    main()
