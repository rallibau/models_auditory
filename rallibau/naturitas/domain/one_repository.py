import abc

from naturitas.domain.one import One


class OneRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, instance_of_one: One) -> int:
        ...

    @abc.abstractmethod
    def get(self, id: int) -> One:
        ...
