from numba import jit
import numpy as np
from numba import jit
from .functions_basic import *


@jit(nopython = True)
def get_uniform(size_population, size_breeding, size_mutation):
    selected_elements = np.random.choice(size_population, size_breeding, replace=False)
    np.random.shuffle(selected_elements)
    #
    parent1 = selected_elements[:int(size_breeding/2)]
    parent2 = selected_elements[int(size_breeding/2):]

    mutations = np.random.choice(size_population, size_mutation, replace=False)

    return parent1, parent2, mutations

# @jit(nopython = True)
def get_lottery(size_population, size_breeding, size_mutation, fitness):
    p = (1/fitness) / np.sum(1/fitness)
    selected_elements = np.random.choice(size_population, size_breeding, replace=False, p = p)
    np.random.shuffle(selected_elements)
    #
    parent1 = selected_elements[:int(size_breeding/2)]
    parent2 = selected_elements[int(size_breeding/2):]
    
    mutations = np.random.choice(size_population, size_mutation, replace=False, p = p)
    return parent1, parent2, mutations

@jit(nopython = True)
def get_elitist(size_breeding, size_mutation, fitness):
    selected_elements = np.argsort(fitness); 
    selected_elements_crossover = selected_elements[:size_breeding]
    np.random.shuffle(selected_elements_crossover)
    #
    parent1 = selected_elements[:int(size_breeding/2)]
    parent2 = selected_elements[int(size_breeding/2):]

    mutations = selected_elements[:size_mutation]
    return parent1, parent2, mutations


@jit(nopython = True)
def get_tournament(size_population, size_tournament, fitness, size_breeding, top_perc = 10):
    selected_elements = np.zeros(size_population, dtype = np.int32)
    n = 0
    while n<size_population:
        subselect = np.random.choice(size_population, size_tournament, replace = False)
        #
        b = np.zeros(subselect.shape[0])
        for i in range(subselect.shape[0]):
            b[i] = fitness[subselect[i]]
        b = np.argsort(b)

        for i in range(int(size_tournament*top_perc/100)):
            selected_elements[n] = subselect[b[i]]
            n+=1
    np.random.shuffle(selected_elements)
    
    parent1 = selected_elements[:int(size_breeding/2)]
    parent2 = selected_elements[int(size_breeding/2):size_breeding]
    mutations = selected_elements[size_breeding:]            
    return parent1, parent2, mutations


@jit(nopython = True)
def generate_childs(population, parent1,parent2):
    childs = np.zeros((parent1.shape[0]*2,30))
    for i in range(parent1.shape[0]):
        child1, child2 = crossover(population[parent1[i],:], population[parent2[i],:]) 
        childs[i*2,:] = child1
        childs[i*2+1,:] = child2
    return childs


@jit(nopython = True)
def generate_mutations(population, mutations):
    mutants = np.zeros((mutations.shape[0],30))
    for i in range(mutations.shape[0]):
        mutants[i,:] = calc_mutation(population[mutations[i],:], n = 1)
    return mutants


@jit(nopython = True)
def get_new_pop(population, parent1, parent2, mutations):
    childs = generate_childs(population, parent1, parent2)
    mutants = generate_mutations(population, mutations)
    pop = np.vstack((childs, mutants))
    pop = pop.astype(np.int32)
    return pop
