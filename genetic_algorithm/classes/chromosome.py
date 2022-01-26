import numpy as np

from genetic_algorithm.classes.base_classes import ChromosomeBase


class Chromosome(ChromosomeBase):
    """
    Chromosome class. A chromosome represents an individual solution
    within the solution space.
    """
    def __init__(self, genotype=None):
        self._source = None
        self._generation = None
        self.genotype = genotype

    def __repr__(self):
        # User-friendly display of the chromosome
        pass

    @property
    def generation(self):
        """Returns at which generation the chromosome was generated."""
        return self._generation

    @generation.setter
    def generation(self, value):
        if not isinstance(value, int):
            raise ValueError("Value {} is not a supported type. Only integer values are allowed.".format(value))
        
        self._generation = value

    @property
    def source(self):
        """Returns the source of the chromosome, i.e, one of 
        'initial_population', 'crossover', 'mutation', 'repair'.
        """
        return self._source

    @source.setter
    def source(self, value):
        if not value in ["initial_population", "crossover", "mutation", "repair"]:
            raise(ValueError("Source {} is not a supported type".format(value)))
        
        self._source = value

    def mutate(self):
        """
        Performs a mutation operation on the instance itself.
        Args:

        Returns -> Mutated chromosome instance
        """
        pass
