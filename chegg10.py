
import numpy as np   #import numpy library
'''PART 1'''
def tenths(xmax):
    '''This function takes an argument 𝑥max and prints out the values of 𝑥^2−𝑥/2 for 𝑥=0.1,0.2,0.3,…,𝑥max (inclusive).'''
    print("The values of 𝑥^2−𝑥/2 for 𝑥=0.1,0.2,0.3,…,𝑥max (inclusive) are :")
    for x in np.arange(0.1,xmax+0.1,0.1):  #we use arange(start,end,step) in numpy to get values 0.1,0.2,0.3 and so on till xmax
                                           #since arange() returns values till end-step we add 0.1 to it so that we get
                                           #xmax value also,, step is the value by which x gets incremented in each iteration
        print(x**2 - x/2)    #print x^2-x/2

xmax=float(input("Enter xmax : "))
tenths(xmax)


'''-----PART 2---------'''
def magnitude(vector):
    '''this function takes one argument 'vector ' which is a three-element tuple representing a Cartesian vector (x, y, z),
     and returns the magnitude of that vector.'''
    x,y,z=vector    #unpack values to variables
    #magnitude= sqrt(x^2+y^2+z^2)
    return np.sqrt(x**2+y**2+z**2)   #return magnitude
#take user input
x=float(input("Enter x : "))
y=float(input("Enter y : "))
z=float(input("Enter z : "))
#call function to print magnitude
print("Magnitude = ",magnitude((x,y,z)))