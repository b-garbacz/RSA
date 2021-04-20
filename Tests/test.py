import time
from main import emulator_rsa
from matplotlib import pyplot as plt
import numpy as np

filepath =  "test.txt"
tab_of_times = []
tab_of_all_times = []
tab_of_means = []
tab_of_bits =[]

for i in range(32,2049):
    start = time.time()
    emulator_rsa(i)
    endtime = time.time() - start
    tab_of_times.append(endtime)

for i in range(32,2049):
    tab_of_bits.append(i)

y = tab_of_times
x = tab_of_bits
plt.title("Program runtime analysis ")
plt.xlabel("Module length in bits")
plt.ylabel("Time")
plt.plot(x,y)
plt.show()

y = tab_of_times
x = tab_of_bits
plt.title("Program runtime analysis (scatter plot)")
plt.xlabel("Module length in bits")
plt.ylabel("Time")
plt.plot(x,y,"ob")
plt.show()

f = open(filepath, "w", encoding="ascii")
for j in range(4,12):
    for i in range(0,101):
        exp = 2**j
        start = time.time()
        emulator_rsa(exp)
        endtime = time.time() - start
        tab_of_times.append(endtime)
    tab_of_all_times.append(tab_of_times)
    del tab_of_times
    tab_of_times = []

for i in range(0,len(tab_of_all_times)):
    tab_of_means.append(np.mean(tab_of_all_times[i]))


x=16
for i in range(0, len(tab_of_means)):
    f.write(str(x)+ "bits" +'\t' +str(tab_of_means[i])+ '\n')
    x *= 2
print("done")
f.close()

