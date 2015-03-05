lam=1E-6;
a=9;
c=3E8;
w=2*pi/lam;
k=w/c;
za=-1/4;
zb=1/4;
z=linspace(za,zb,1000);
t=[0,5/6,5/3,2.5,10/3];
for i=1:5 
	subplot(1,5,i)
	plot(z,2*a*cos(w*t(i))*cos(k*z))
end