from .problem import *
from .functions_pop import *
from .functions_basic import check_pop
#from numba import cuda
import time

class follow_time():
    def __init__(self):
        self.t0 = time.time()
        pass

    def update(self):
        t1=time.time()
        delta = t1-self.t0
        self.t0 = t1
        return delta



class geneticAlgo:
    def __init__(self, size_population:int, ratio_breeding:float, 
                 size_tournament:int, gene_size:int):
        self.size_population = size_population
        self.ratio_breeding = ratio_breeding
        self.size_tournament = size_tournament
        self.gene_size = gene_size
        self.matrix = load_data_TSP1()
        self.L_options = ["uniform", "elitist", "lottery", "tournament", "random"]

        self.test_1 = np.array([np.sum([i for i in range(self.gene_size)])])
        self.test_2 = np.array([i*self.size_population for i in range(self.gene_size)])


        self.size_breeding = int(size_population*ratio_breeding)
        if self.size_breeding % 2 !=0:
            self.size_breeding = self.size_breeding-1

        self.size_mutation = int(self.size_population-self.size_breeding)

        self.name_indicators = ["best_fitness","average_fitness","diversity", "fitness_variance"]
        self.reset_indicators()


    def reset_indicators(self):
        self.indicators = {}
        for n in self.name_indicators:
            self.indicators[n] = []


    def create_population(self, check:bool = False):
        self.reset_indicators()
        self.population = np.array([np.random.permutation(self.gene_size) for _ in range(self.size_population)], dtype=np.int64)
        self.update_fitness()
        self.calculate_indicators()
        self.n_gen = 1
        if check: self.check_pop()


    def check_pop(self):
        pop_sorted = np.sort(self.population, axis = 1)
        t_1 = np.sum(pop_sorted, axis = 1)
        t_2 = np.sum(pop_sorted, axis = 0)
        if (t_1==self.test_1).all() and (t_2==self.test_2).all():
            print("Population checked: fine.")
        else:
            print("Population checked: error.")


    def next_gen(self, option:str, check:bool = False):
        if option not in self.L_options:
            print(f"option {option} not available, please select value in {self.L_options}")

        if option == "uniform":
            parent1, parent2, mutations = get_uniform(self.size_population, 
                                                      self.size_breeding, 
                                                      self.size_mutation)
            #
        elif option == "elitist":
            parent1, parent2, mutations = get_elitist(self.size_breeding, 
                                                      self.size_mutation, 
                                                      self.fitness)
        elif option == "lottery":
            parent1, parent2, mutations = get_lottery(self.size_population,
                                                      self.size_breeding, 
                                                      self.size_mutation, 
                                                      self.fitness)
        elif option == "tournament":
            parent1, parent2, mutations = get_tournament(self.size_population, 
                                                         self.size_tournament, 
                                                         self.fitness, 
                                                         self.size_breeding, 
                                                         top_perc = 10)

        if option == "random":
            self.population = np.array([np.random.permutation(self.gene_size) for _ in range(self.size_population)], dtype=np.int64)
        elif option != "random":
            """
            print(self.population.shape, self.population.dtype)
            print(parent1.shape, parent1.dtype)
            print(parent2.shape, parent2.dtype)
            print(mutations.shape, mutations.dtype)
            """

            self.population = get_new_pop(self.population, parent1 = parent1, parent2 = parent2, mutations = mutations)
        self.update_fitness()
        self.calculate_indicators()
        self.n_gen +=1
        if check: self.check_pop()


    def update_fitness(self):
        self.fitness = get_fitness(self.population, self.matrix)
        

    def calculate_indicators(self):
        self.indicators["best_fitness"].append(np.min(self.fitness))
        self.indicators["average_fitness"].append(np.mean(self.fitness))
        self.indicators["fitness_variance"].append(np.std(self.fitness))