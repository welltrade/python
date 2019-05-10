import random
import matplotlib.pyplot as plt

l = 20
dt =[]
x = random.randint(0, 100)
dt.append(x)
i = 0
while i < l:
    dt.append(x + random.choice([-1, -1, -1, 0, 1, 1, 1,]) + random.choice([-0.5, -0.25, 0, 0.25, 0.5]) + random.choice([-0.5, -0.25, 0, 0.25, 0.5]))
    i += 1
    
#print(dt) 

plt.plot(list(range(0, l + 1)), dt, 'ro')
plt.axis([0, l + 2 , min(dt) - 2, max(dt) + 2])
plt.show()

