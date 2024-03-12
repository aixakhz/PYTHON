#HW 5: Numpy Arrays
#Hey Twin
import numpy as np

myArray=np.array([[1,1,1],[1,2,3],[2,2,2]])
print(np.unique(myArray,return_counts=True,axis=1))

#Checkers
x=np.zeros((8,8), dtype=int)
x[1::2,::2]=1
x[::2,1::2]=1
print(x) #for this problem, I looked up the problem and the website that...
#helped was "https://www.w3resource.com/python-exercises...
#/numpy/python-numpy-exercise-10.php"

#I need some space
arr=np.array(['python','is','cool!'])
def separate_letters_with_space(arr):
    separated_array=np.array([' '.join(word) for word in arr])
    return separated_array
result=separate_letters_with_space(arr)
print(result)

#Everything is in order
np.random.seed(12345)
a=np.random.randint(1,50,(4,5))
def sorting(matrix):
    sorted_matrix=np.sort(matrix,axis=0)
    return sorted_matrix
print("original matrix:")
print(a)
print("\nSorted matring along columns:")
print(sorting(a))
#I used the numpy website to help with commands alongside some...
#floormates that are cs majors