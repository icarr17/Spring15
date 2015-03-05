from pylab import *
import matplotlib.pyplot as plt
lam=1E-6;
a=9.;
c=3E8;
w=2.*pi/lam;
k=w/c;
za=-1./4;
zb=1./4;
z=linspace(za,zb,1000);
t=[0,5./6,5./3,2.5,10./3];
for i in range(0,5):
	plt.subplot(1,5,i+1)
	plt.plot(z,2.*a*cos(w*t[i]*10**(-12))*cos(k*z))
show()

va=1E12
vb=1.05E12
t=linspace(0,.5/(vb-va),1000)
ua=7*cos(2.*pi*va*t)
ub=7*cos(2.*pi*vb*t)

plot(t,ua)
plot(t,ub)
show()

t=linspace(0,3*.5/(vb-va),3*1000)
ua=7*cos(2.*pi*va*t)
ub=7*cos(2.*pi*vb*t)
u = [ua[i]+ub[i] for i in range(len(ua))]
plot(t,u)
show()