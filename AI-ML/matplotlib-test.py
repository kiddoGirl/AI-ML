import matplotlib.pyplot as plt
import numpy as np

m1 = np.array([0,2,4,6,10])
m2 = np.array([10,30,60,100,250])

font1 = {'family' : 'serif' , 'color' : 'blue' , 'size' : 20 }
font2 = {'family' : 'serif' , 'color' : 'red' , 'size' : 20 }

plt.subplot(2,3,1)
plt.plot(m1 ,'o:' ,  ms='30' , mec = 'k' , mfc = 'b')
plt.plot(m2 ,'o--', ms='10' , mec='r' , mfc = 'y')

plt.title('matplotlib testing' , fontdict=font1)
plt.xlabel('manju' , fontdict=font2)
plt.ylabel('bashini' , fontdict=font2)

plt.grid(color='green' , linestyle='--' , linewidth = 0.5)


m3 = np.array([0,1,4,5,7])
m4 = np.array([10,20,30,40,50])

plt.subplot(2,3,2)
plt.plot(m3,m4)
plt.title('food')



m5 = np.array([0,1,4,5,7])
m6 = np.array([10,20,30,40,50])

plt.subplot(2,3,3)
plt.plot(m5,m6)
plt.title('meow')



m7 = np.array([0,1,4,5,7])
m8 = np.array([10,20,30,40,50])

plt.subplot(2,3,4)
plt.plot(m7,m8)
plt.title('food')


m9 = np.array([0,1,4,5,7])
m10 = np.array([10,20,30,40,50])

plt.subplot(2,3,5)
plt.plot(m9,m10)
plt.title('food')


m11 = np.array([0,1,4,5,7])
m12 = np.array([10,20,30,40,50])

plt.subplot(2,3,6)
plt.plot(m11,m12)
plt.title('food')





plt.show()
