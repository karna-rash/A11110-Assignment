import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy 

simlen = 1000000
gen = np.loadtxt('./uni.dat',dtype='double')

c1 =np.zeros(40)
c2=np.linspace(0,1,10)
c3=np.ones(30)
c =np.concatenate([c1,c2,c3])
x = np.linspace(-4,4,80)
CF=[]
for i in range(0,80):
	CF_ind = np.nonzero(gen < x[i]) 
	CF_n = np.size(CF_ind)
	CF.append(CF_n/simlen) 

#def uni_cdf(x):
#	if 0 <= x:
#		return x
#	elif x < 0 :
#	      return 0
#	else:
#	   return 1


#f2=np.vectorize(uni_cdf)

plt.plot(x.T,CF,"o")
plt.plot(x.T,c)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])
plt.savefig("../figs/uni_cdf.pdf")
plt.savefig("../figs/uni_cdf.eps")
plt.show()
