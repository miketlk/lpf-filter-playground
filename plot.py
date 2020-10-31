import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        x.append(i)
        y.append(float(row[0]))

plt.plot(x,y, label='Output signal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Step response of LPF filter')
plt.legend()
plt.show()