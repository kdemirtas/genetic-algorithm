import os
import unittest

import numpy as np

from genetic_algorithm.utils.helpers import ensure_np_array
from genetic_algorithm.utils.operators import Operator
from genetic_algorithm.classes.chromosome import Chromosome


class TestOperators(unittest.TestCase):

    def setUp(self):
        self.gene1 = np.array([3, 4, 5, 6, 7])
        self.chromosome1 = Chromosome(genotype=self.gene1)

        self.gene2 = np.array([0, 0, 1, 1, 2])
        self.chromosome2 = Chromosome(genotype=self.gene2)

        self.op = Operator()

    def tearDown(self):
        pass

    def test_operators_single_point_crossover_correct(self):
        chromosomes = [self.chromosome1, self.chromosome2]
        children = self.op._uniform_crossover(chromosomes, cutoff=0.5)
        child1_gen = children[0].genotype
        child2_gen = children[1].genotype
        children_genes = ensure_np_array([child1_gen, child2_gen])
        child1_gen = np.array([3, 4, 1, 1, 2])
        child2_gen = np.array([0, 0, 5, 6, 7])
        children_genes_expected = np.array([child1_gen, child2_gen])
        self.assertTrue(np.array_equal(children_genes, children_genes_expected))

    def test_operators_crossover_calls_uniform_correct(self):
        pass

    def test_operators_crossover_uniform(self):
        pass

    def test_operators_crossover_single_point(self):
        pass

    def test_operators_crossover_multiple_points(self):
        pass



if __name__ == "__main__":
    unittest.main()