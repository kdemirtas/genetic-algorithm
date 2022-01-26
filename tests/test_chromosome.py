import os
import unittest

from genetic_algorithm.classes.chromosome import Chromosome


class TestChromosome(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_chromosome_source_none_for_empty_chromosome(self):
        c = Chromosome()
        self.assertIsNone(c.source)

    def test_chromosome_set_source_correct(self):
        c = Chromosome()

        c.source = "initial_population"
        self.assertEqual(c.source, "initial_population")
        c.source = "crossover"
        self.assertEqual(c.source, "crossover")
        c.source = "mutation"
        self.assertEqual(c.source, "mutation")
        c.source = "repair"
        self.assertEqual(c.source, "repair")

    def test_chromosome_set_unsupported_source(self):
        c = Chromosome()

        with self.assertRaises(ValueError):
            c.source = "unsupported_source"

    def test_chromosome_set_generation_correct(self):
        c = Chromosome()
        c.generation = 7
        self.assertEqual(c.generation, 7)

    def test_chromosome_set_generation_unsupported(self):
        c = Chromosome()
        with self.assertRaises(ValueError):
            c.generation = 3.14


if __name__ == "__main__":
    unittest.main()