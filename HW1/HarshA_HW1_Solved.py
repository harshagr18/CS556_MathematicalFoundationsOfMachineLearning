#!/usr/bin/env python
# coding: utf-8

# In[1]:


def MatrixAddition(A,B):

    C=[]

    if len(A[0])!=len(B[0]) or len(A)!=len(B):
        print("Addition is not possible")
        return
    else:
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                temp.append(A[i][j]+B[i][j])
            C.append(temp)
    print(C)
    return        


## Test cases for addition
A=[[ 1,2], [3,4]] 
B=[[5,6,7], [7,8,8]]

B=[[5,6,7], [7,8,8]]
C=[[15,16,17], [27,28,28]]

MatrixAddition(A,B)

MatrixAddition(C,B)


# In[2]:


def MatrixMultiplication(A,B):
    
    if len(A[0]) != len(B):
        print("Multiplication is not possible")
        return
    else:
        rows = len(A)
        cols = len(B[0])
        C = [([0]*cols) for i in range(rows)]
        
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
        print(C)
        return


A=[[ 1,2,3], [3,4,5],[7,8,9]] # 3x3
B=[[5,6,7], [7,8,8],[8,9,7]] # 3x3
MatrixMultiplication(A,B)

A= [[5,6,7],[7,8,8],[8,9,7]] # 3x3
B =[[1,2,3],[3,4,5]] # 2x3
MatrixMultiplication(A,B)


# In[3]:


def MatrixTranspose(A):
    B = []
    
    for i in range(len(A[0])):
        temp = []
        for j in range(len(A)):
            temp.append(A[j][i])
        B.append(temp)
    print(B)
    return 
    

A=[[ 1,2,3], [3,4,5]] 
MatrixTranspose(A)


B=[[5,6], [7,8],[8,9]]
MatrixTranspose(B)

# “I pledge my honor that I have abided by the Stevens Honor System.” 
