from typing import Dict, List, Set, Type

from naturitas.actions.subs.internal import DomainObjectUpdatedSub
from naturitas.domain.domain_object_updated import DomainObjectUpdated
from naturitas.domain.events import EventSubscriber, Event
from naturitas.domain.publishers import InternalEventPublisher


class InMemoryInternalEventPublisher(InternalEventPublisher):
    HANDLERS: Dict[Type[Event], Set[Type[EventSubscriber]]] = {
        DomainObjectUpdated: {DomainObjectUpdatedSub},
    }

    def publish(self, events: List[Event]) -> None:
        for event in events:
            handlers = self.HANDLERS[event.__class__]

            for handler in handlers:
                handler().on(event)
