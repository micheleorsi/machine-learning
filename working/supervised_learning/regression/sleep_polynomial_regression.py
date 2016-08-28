#
#	Polynomial Regression
#
#	In this exercise we will examine more complex models of test grades as a function of
#	sleep using numpy.polyfit to determine a good relationship and incorporating more data.
#
#
#   at the end, store the coefficients of the polynomial you found in coeffs
#

import numpy as np
import matplotlib.pyplot as plt

sleep = [5,6,7,8,10,12,16]
scores = [65,51,75,75,86,80,0]

deg_1 = np.polyfit(sleep, scores, 1)
deg_2 = np.polyfit(sleep, scores, 2)
deg_3 = np.polyfit(sleep, scores, 3)
deg_4 = np.polyfit(sleep, scores, 4)


plt.scatter(sleep, scores)

plt.plot(sleep, np.polyval(deg_1, sleep),color='red')
plt.plot(sleep, np.polyval(deg_2, sleep),color='blue')
plt.plot(sleep, np.polyval(deg_3, sleep),color='green')
plt.plot(sleep, np.polyval(deg_4, sleep),color='black')

plt.show()

coeffs = deg_2
