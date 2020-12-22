import json
import random
from models.Model import Model
from models.instances import Instances


class Phenotype(object):

    def __init__(self, phenotype_id, committee, gen_length):
        # phenotype attributes
        self.__id = phenotype_id
        self.__committee = committee
        self.__genLength = gen_length
        self.__fitness = 0.0
        self.__normalizedFitness = 0.0
        self.__genes = [False for x in range(self.gen_length)]
        # classifier attribute
        self.__predictions = []
        self.__model = Model()
        self.__inst = Instances()
        self.create_random_genes()

    @property
    def committee(self):
        return self.__committee

    @committee.setter
    def committee(self, value):
        if value > 0:
            self.__committee = value

    @property
    def gen_length(self):
        return self.__genLength

    @property
    def genes(self):
        return self.__genes

    @genes.setter
    def genes(self, value):
        if len(value) == self.gen_length:
            self.__genes = value

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, value):
        if value >= 0.0:
            self.__fitness = value

    @property
    def normalizedFitness(self):
        return self.__normalizedFitness

    @normalizedFitness.setter
    def normalizedFitness(self, value):
        if 0.0 <= value <= 1.0:
            self.__normalizedFitness = value

    def copy(self, donor):
        self.__committee = donor.committee
        self.__genLength = donor.gen_length
        self.__fitness = donor.fitness
        self.__normalizedFitness = donor.normalizedFitness
        self.__genes = donor.genes

    # generate 10 positive genes (classifiers)
    def create_random_genes(self):
        it = 0
        while it < self.committee:
            index = random.randint(0, self.gen_length - 1)
            if not self.genes[index]:
                self.genes[index] = True
                it += 1

    # Take results, vote for answer and calc score, then penalize bigger committees
    def calc_fitness(self):
        committee_answers = []
        for i in range(len(self.__predictions[0])):
            tmp = {}
            for predicts in self.__predictions:
                if predicts[i] in tmp.keys():
                    tmp[predicts[i]] += 1
                else:
                    tmp[predicts[i]] = 1
            inverse = [(value, key) for key, value in tmp.items()]
            val = max(inverse)[1]
            committee_answers.append(val)
        self.__fitness = 0.8 * pow(self.__model.calcScore(predictions=committee_answers, verify=False) + 1, 2) + \
                         0.2 * 0.05 * (self.gen_length / self.__committee)
        return self.__fitness

    # choose classifiers from list and execute
    # then calculate fitness of all
    def run(self):
        self.__predictions.clear()
        for i, gen in enumerate(self.genes):
            if gen:
                # Different approach
                #  score, predictions = self.__model.runClassifier(self.__inst.trained_classifiers[i])
                #  self.__scores.append(score)
                #  self.__predictions.append(predictions)
                self.__predictions.append(self.__inst.predictions_arr[i])

        return self.calc_fitness()

    # Just for testing
    def test(self):
        pass
