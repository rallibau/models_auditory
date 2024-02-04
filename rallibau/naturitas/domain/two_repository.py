import abc

from naturitas.domain.one import One
from naturitas.domain.two import Two


class TwoRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, instance_of_two: Two) -> int:
        ...

    @abc.abstractmethod
    def get(self, id: int) -> One:
        ...

