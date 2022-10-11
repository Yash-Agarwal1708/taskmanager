import numpy
r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]
#value of dim depend on the NxN matrix we want so does the no. of r_n and s_n we introduce.


s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

B=[]
B.append(s1)
B.append(s2)
B.append(s3)


#i need 0 matrix
x= numpy.mat(A)
y= numpy.mat(B)
print (x*y)