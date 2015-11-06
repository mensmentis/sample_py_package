from sample_py_package.operations.addition import add
from sample_py_package.operations.subtraction import sub
import matplotlib.pyplot as plt

def visual():
    added = []
    subed = []
    z = [[2.14, 53.2], [67.2, 34.7], [91.5, 12.4], [9.1, 1.2], [64.2, 77.3]]

    for i in z:
        added.append(add(i[0], i[1]))
        subed.append(sub(i[0], i[1]))

    plt.plot(added, 'r')
    plt.plot(subed, 'g')
    plt.show()
