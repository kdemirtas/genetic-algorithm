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

        self.chromosomes = ensure_np_array([self.chromosome1, self.chromosome2])

        self.op = Operator()

    def tearDown(self):
        pass

    def test_operators_single_point_crossover_correct_with_cutoff(self):
        children = self.op._single_point_crossover(self.chromosomes, cutoff=0.5)
        child1_gen = children[0].genotype
        child2_gen = children[1].genotype
        children_genes = ensure_np_array([child1_gen, child2_gen])
        child1_gen = np.array([3, 4, 1, 1, 2])
        child2_gen = np.array([0, 0, 5, 6, 7])
        children_genes_expected = np.array([child1_gen, child2_gen])
        self.assertTrue(np.array_equal(children_genes, children_genes_expected))

    def test_operators_single_point_crossover_raises_value_error_for_bad_cutoff_value(self):
        with self.assertRaises(ValueError):
            children = self.op._single_point_crossover(self.chromosomes, cutoff=1.5)
 

    def test_operators_single_point_crossover_correct_no_cutoff(self):
        children = self.op._single_point_crossover(self.chromosomes)
        self.assertTrue(len(children), 2)

    def test_operators_crossover_calls_single_point_correct_with_cutoff(self):
        args = {
            "cutoff_proportion": 0.5
        }
        children = self.op.crossover(self.chromosomes, crossover_type="single-point", args=args)
        child1_gen = children[0].genotype
        child2_gen = children[1].genotype
        children_genes = ensure_np_array([child1_gen, child2_gen])

        child1_gen_expected = np.array([3, 4, 1, 1, 2])
        child2_gen_expected = np.array([0, 0, 5, 6, 7])
        children_genes_expected = np.array([child1_gen_expected, child2_gen_expected])
        
        self.assertTrue(np.array_equal(children_genes, children_genes_expected))

    def test_operators_crossover_calls_single_point_correct_no_cutoff(self):
            children = self.op.crossover(self.chromosomes, crossover_type="single-point")
            self.assertTrue(len(children), 2)

    def test_operators_uniform_crossover_correct_with_uniform_mask(self):
        uniform_mask = np.array([0, 0, 1, 1, 0])
        children = self.op._uniform_crossover(self.chromosomes, uniform_mask=uniform_mask)
        child1_gen = children[0].genotype
        child2_gen = children[1].genotype
        children_genes = ensure_np_array([child1_gen, child2_gen])
        
        child1_gen_expected = np.array([3, 4, 1, 1, 7])
        child2_gen_expected = np.array([0, 0, 5, 6, 2])
        children_genes_expected = np.array([child1_gen_expected, child2_gen_expected])
        
        self.assertTrue(np.array_equal(children_genes, children_genes_expected))

    def test_operators_uniform_crossover_correct_with_no_uniform_mask(self):
            children = self.op._uniform_crossover(self.chromosomes)
            self.assertTrue(len(children), 2)

    def test_operators_crossover_calls_uniform_correct_with_uniform_mask(self):
        uniform_mask = np.array([0, 0, 1, 1, 0])
        args = {
            "uniform_mask": uniform_mask
        }
        children = self.op.crossover(self.chromosomes, crossover_type="uniform", args=args)
        child1_gen = children[0].genotype
        child2_gen = children[1].genotype
        children_genes = ensure_np_array([child1_gen, child2_gen])

        child1_gen_expected = np.array([3, 4, 1, 1, 7])
        child2_gen_expected = np.array([0, 0, 5, 6, 2])
        children_genes_expected = np.array([child1_gen_expected, child2_gen_expected])
        
        self.assertTrue(np.array_equal(children_genes, children_genes_expected))

    def test_operators_crossover_calls_uniform_correct_with_no_uniform_mask(self):
            children = self.op.crossover(self.chromosomes, crossover_type="uniform")
            self.assertTrue(len(children), 2)

if __name__ == "__main__":
    unittest.main()