import matplotlib.pyplot as plt
import random
import math

n=2000
count=0
data = []
data2 = []

for i in range(n):
  x1=random.uniform(-1,1)
  y1=random.uniform(-1,1)
  if (x1 * x1 + y1 * y1 < 1):
    data2.append([x1,y1])
  else:
    data.append([x1,y1])

plt.figure(figsize = (8,8))

x, y = zip(*data)
plt.scatter(x, y)

x, y = zip(*data2)
plt.scatter(x, y)

plt.show()

Pi = 4 * len(data2)/n
print(f"Pi : {Pi}")
print(f"Difference: {round(abs(math.pi - Pi),4)}")
