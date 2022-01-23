import numpy as np
import utils.helpers as hp


class Chromosome:
    """
    Chromosome class. A chromosome represents an individual solution
    within the solution space.
    """
    def __init__(self):
        pass

    def __repr__(self):
        # User-friendly display of the chromosome
        pass

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
