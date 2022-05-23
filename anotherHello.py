import math 
import numpy as np
import matplotlib.pyplot as plt

arrayX = []
arrayY = []
start = 0
end = 365
inc = 5

for i in range(start, end, inc):
    arrayX.append(i)
    
for i in range(start, end, inc):
    arrayY.append(np.sin(i*math.pi/180))

x = arrayX
y = arrayY

plt.plot(x, y, color = 'green', marker = "o")
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.grid(color='r', linestyle='-', linewidth=0.2)
plt.title('Constant Complexity')
plt.xticks(np.arange(0, 370, step = 45))
plt.show()
