### Question 1:
# Write a function to sum N natural numbers without using sum-function

def sumNaturalNumbers(n):
  sum = 0
  for i in range(n+1):
    sum = sum+i
    
  return sum

sumNaturalNumbers(10)


### Question 2:
# Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.1428*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.1428*self.radius
    
Circle(10).area()


## Question 3:
# Timer
import time
def timer(fn):
    def inner(*args,**kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print('Time taken to execute {} is {} secs'.format(fn.__name__, (time.time()-start)))
        return result
    return inner
 
## Question 4:
# Counter
def counter(fn):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count= count+1
        result = fn(*args, **kwargs)
        print('{} is executed {} times'.format(fn.__name__, count))
        return result
    return inner
