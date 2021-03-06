# Needs a evolve object
import evo_object as evo_object
import random
import math
from copy import deepcopy

# HELPER FUNCTIONS

class Evolve_population:

    # initializes population
    def __init__(self, my_total_population, my_mutation_parameter, 
                 my_cross_pollination_parameter, monograms, bigrams,
                 line_types, a, A, B, C, D):
        self.mutation_parameter = my_mutation_parameter
        self.cross_pollination_parameter = my_cross_pollination_parameter
        self.total_population = my_total_population
        self.monograms = monograms
        self.bigrams = bigrams
        self.line_types = line_types
        self.a = a
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        
        self.population_list = []
                
        for x in range (0, my_total_population):
            # Creates new object
            new_object = evo_object.gen_random_evo(self.monograms, self.bigrams,
                        self.line_types, self.a, self.A, self.B, self.C, self.D)
            self.population_list.append(new_object)
        # sorts the list
        self.population_list.sort()
            
    # as of now, uniformly chooses elements to mutate
    def create_mutants (self,base_population):
        x = random.randint(0, len(base_population)- 1)
        to_be_mutated = base_population[x]
        mutated_object = evo_object.mutate(to_be_mutated, self.monograms,
                    self.bigrams, self.a, self.A, self.B, self.C, self.D)
        return mutated_object

    # similarly, uniformly chooses elements to cross_pollinate
    # Note that if it chooses the same one, it will effectively replicate the said object, which is not bad
    def create_cross_pollinated (self,base_population):
        x = random.randint(0, len(base_population) - 1)
        y = random.randint(0, len(base_population) - 1)
        pollinated_object = evo_object.cross_pollinate (base_population[x], 
                            base_population[y], self.monograms, self.bigrams,
                            self.a, self.A, self.B, self.C, self.D)
        return pollinated_object

    def update_next_generation(self):
        mutant_pop = int(self.total_population * self.mutation_parameter)
        cross_pop = int(self.total_population * self.cross_pollination_parameter)
        prev_pop = deepcopy(self.population_list)
        # Creates random pollination/mutation
        for x in range (0, mutant_pop):
            new_mutant = self.create_mutants(prev_pop)
            self.population_list.append (new_mutant)
        for x in range (0, cross_pop):
            new_cross = self.create_cross_pollinated(prev_pop)
            self.population_list.append (new_cross)    
        # sorts it
        self.population_list.sort()
        # gets rid of repetition and cuts off the least successful ones
        to_live_on = []
        set_haiku = False
        last_haiku = None
        counter = 0
        for haiku in self.population_list:
            if counter >= self.total_population:
                break
            if (not set_haiku) or haiku != last_haiku:
                to_live_on.append(haiku)
                last_haiku = haiku
                set_haiku = True
                counter += 1
        self.population_list = to_live_on
#       self.population_list = self.population_list[:self.total_population]

