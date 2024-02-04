import abc

from naturitas.domain.Auditory import Auditory


class AuditoryRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, auditory: Auditory) -> int:
        ...
