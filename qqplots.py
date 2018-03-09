import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

s = [42.1, 51.0, 30.0, 35.2, 29.3, 10.9, 16.1, 51.6,
     47.0, 51.4, 35.2, 31.7, 17.8, 67.0, 43.2, 23.7,
     25.2, 36.1, 32.3, 51.7, 46.0, 12.2, 21.1, 29.0,
     14.3, 47.2, 31.3, 35.4, 29.1, 23.0, 10.3, 34.2]

plt.hist(s, 6)  # (datos,num_intervalos,
plt.show()



"""
http://connor-johnson.com/2014/12/31/the-pearson-chi-squared-test-with-python-and-r/
N = 1200
p = 0.53
q = 1000
obs = np.random.poisson()

z = (obs-np.mean(obs))/np.std(obs)

stats.probplot(z, dist=stats.poisson(p), plot=plt)
plt.title("Poisson Q-Q plot")
plt.show()

"""
