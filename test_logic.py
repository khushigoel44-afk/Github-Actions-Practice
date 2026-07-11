import sys

def addition(a,b):
    return a + b

res = addition(2, 3)

if res == 5:
    print("The test passed successfully!")
    sys.exit(0)
else:
    print("The test failed!")
    sys.exit(1)

