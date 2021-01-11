import matplotlib.pyplot as plt

import random

n=1000
count=0
data = []
data2 = []
for i in range(n):
  x1=random.uniform(-1,1)
  y1=random.uniform(-1,1)
  if (x1 * x1 + y1 * y1 < 1):
      data2.append([x1,y1])
  data.append([x1,y1])

x, y = zip(*data)
plt.scatter(x, y)

x, y = zip(*data2)
plt.scatter(x, y)
plt.figure(figsize=(12, 12))

plt.show()
