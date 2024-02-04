from datetime import datetime

from naturitas.domain.domain_object_updated import DomainObjectUpdated
from naturitas.domain.one import One
from naturitas.domain.one_repository import OneRepository
from naturitas.domain.publishers import InternalEventPublisher


class SaveOne:
    def __init__(self, one_repo: OneRepository, internal_event_publisher: InternalEventPublisher):
        self.one_repo = one_repo
        self.internal_event_publisher = internal_event_publisher

    def execute(self, one: One, user: str) -> int:
        data_before_change = {}
        if one.id:
            before_instance = self.one_repo.get(one.id)
            data_before_change = before_instance.to_json()
        id = self.one_repo.save(one)
        self.internal_event_publisher.publish([
            DomainObjectUpdated(
                change_date=datetime.now(),
                user=user,
                model_name="one",
                model_instance_id=id,
                data_before_change=data_before_change,
                data_after_change=one.to_json(),
            )
        ])
        return id
