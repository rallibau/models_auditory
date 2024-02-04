import abc
from dataclasses import asdict, dataclass
from typing import Generic, List, TypeVar

T = TypeVar("T", bound="Event")


@dataclass(frozen=True)
class Event:
    def to_dict(self) -> dict:
        return asdict(self)


class EventSubscriber(abc.ABC, Generic[T]):
    @abc.abstractmethod
    def on(self, event: T) -> None:
        ...


class AggregateRoot:
    def __init__(self) -> None:
        self._events: List[Event] = []

    def register(self, event: Event) -> None:
        self._events.append(event)

    def collect_events(self) -> List[Event]:
        events = self._events
        self._events = []
        return events
