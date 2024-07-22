import numpy as np
from numba import jit
import random
from numba import cuda

@jit(nopython = True)
def get_fitness(a, matrix):
    size = a.shape[0]
    out = np.zeros((size))
    
    for i in np.arange(size):
        summ = 0
        for j in range(29):
            summ = summ + matrix[a[i,j],a[i,j+1]]        
        out[i] = summ
    return out

##########################

@jit(nopython = True)
def calc_mutation(array_in, n = 1):
    array_out = array_in.copy()

    for _ in range(n):
        i0,i1 = np.random.choice(30, 2, replace=False)
        array_out[i0] = array_in[i1]
        array_out[i1] = array_in[i0]
        if n > 1:
            array_in = array_out.copy()
    return array_out

@jit(nopython = True)
def create_child(parent1, parent2, size, a,b):
    child = np.full(size, -1)

    for index in range(a,b):
        child[index] = parent1[index]

    idx = 0
    for gene in parent2:
        if gene not in child:
            while child[idx] != -1:
                idx += 1
            child[idx] = gene
    return child

@jit(nopython=True)
def crossover(parent1, parent2):
    size = parent1.shape[0]
    #
    a = random.randint(2,27)
    b = random.randint(a,29)
    child1 = create_child(parent1, parent2, size, a, b)

    a = random.randint(2,27)
    b = random.randint(a,29)
    child2 = create_child(parent1, parent2, size, a, b)
    return child1, child2


@jit(nopython=True)
def check_pop(pop_sorted):
    for i in range(30):
        un = np.unique(pop_sorted[:,i])
        if un.shape[0]!= 1:
            print("error multiple number")
        else:
            if un[0] != i:
                print("error")
        
