from abc import ABC, abstractmethod


class OperatorBase(ABC):  
    @abstractmethod
    def crossover(self):
        pass

    @abstractmethod
    def mutate(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass


class ChromosomeBase(ABC):
    @abstractmethod
    def source(self):
        pass

    @abstractmethod
    def generation(self):
        pass


class PopulationBase(ABC):
    @abstractmethod
    def generation(self):
        pass


class SolverBase(ABC):
    @abstractmethod
    def solve(self):
        pass