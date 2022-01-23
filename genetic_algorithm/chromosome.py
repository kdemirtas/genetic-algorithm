import numpy as np


class Chromosome:
    """
    Chromosome class. A chromosome represents an individual solution
    within the solution space.
    """
    def __init__(self):
        self._source = None
        self._generation = None

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


    def crossover(self, other):
        """
        Takes an other chromosome and performs a crossover with it.
        Args:
            other -> Chromosome instance
        Returns:
            children -> Numpy array of children containing two new chromosome instances
        """
        children = np.array([])

        return children

    def mutate(self):
        """
        Performs a mutation operation on the instance itself.
        Args:

        Returns -> Mutated chromosome instance
        """
        pass
