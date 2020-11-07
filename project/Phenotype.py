import json
import random
import sys

from models import DecisionForest


class Phenotype:

    def __init__(self, committee, gen_length):
        # phenotype attributes
        self.__committee = committee
        self.__genLength = gen_length
        self.__fitness = 0.0
        self.__normalizedFitness = 0.0
        self.__isBest = False
        self.__isClassificationFinished = False
        self.__genes = [False for x in range(self.gen_length)]
        # classifier attributes
        self.__classifiers = {}
        self.__scores = []
        self.__times = []
        self.__predictions = []
        # prep phase
        with open("models/_models_list.json") as f:
            self.__classifiers = json.load(f)
        self.create_random_genes()

    @property
    def committee(self):
        return self.__committee

    @property
    def gen_length(self):
        return self.__genLength

    @property
    def is_best(self):
        return self.__isBest

    @property
    def is_classification_finished(self):
        return self.__isClassificationFinished

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

    # generate 10 positive genes (classifiers)
    def create_random_genes(self):
        it = 0
        while it < self.committee:
            index = random.randint(0, self.gen_length - 1)
            if not self.genes[index]:
                self.genes[index] = True
                it += 1

    def classification_did_finish(self):
        return self.__isClassificationFinished

    def calc_fitness(self):
        pass

    # choose classifiers from list and execute
    # then calculate fitness of all
    def run(self):
        self.__isClassificationFinished = False
        for i, gen in enumerate(self.genes):
            if gen:
                # TODO make more versatile
                if i < 10:
                    s = "0" + str(i)
                else:
                    s = str(i)
                digit1st = s[0]
                digit2nd = s[1]
                # END
                classifier = self.__classifiers[digit1st]["version"][digit2nd]
                filename = getattr(sys.modules[__name__], self.__classifiers[digit1st]["name"])
                method = getattr(filename, classifier, lambda: "Invalid classifier")
                score, time, result = method()
                self.__scores.append(score)
                self.__times.append(time)
                self.__predictions.append(result)
        self.calc_fitness()
        self.__isClassificationFinished = True

    # Just for testing
    def test(self):
        digit1st = "0"
        digit2nd = "0"
        classifier = self.__classifiers[digit1st]["version"][digit2nd]
        method = getattr(getattr(sys.modules[__name__], self.__classifiers[digit1st]["name"]),
                         classifier, lambda: "Invalid classifier")
        method()
