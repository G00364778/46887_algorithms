import matplotlib.pyplot as pl

exp=[i**2 for i in range(0,101)]
pl.plot(exp)
pl.xlabel('Number of array values')
pl.ylabel('Number of comparisons completed')
pl.show()
