import abc
from typing import List

from naturitas.domain.events import Event


class InternalEventPublisher(abc.ABC):
    @abc.abstractmethod
    def publish(self, events: List[Event]) -> None:
        ...
