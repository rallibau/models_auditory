from datetime import datetime

from naturitas.domain.domain_object_updated import DomainObjectUpdated
from naturitas.domain.publishers import InternalEventPublisher
from naturitas.domain.two import Two
from naturitas.domain.two_repository import TwoRepository


class SaveTwo:
    def __init__(
        self, two_repo: TwoRepository, internal_event_publisher: InternalEventPublisher
    ):
        self.two_repo = two_repo
        self.internal_event_publisher = internal_event_publisher

    def execute(self, two: Two, user: str) -> int:
        data_before_change = {}
        if two.id:
            before_instance = self.two_repo.get(two.id)
            data_before_change = before_instance.to_json()
        id = self.two_repo.save(two)
        self.internal_event_publisher.publish(
            [
                DomainObjectUpdated(
                    change_date=datetime.now(),
                    user=user,
                    model_name="two",
                    model_instance_id=id,
                    data_before_change=data_before_change,
                    data_after_change=two.to_json(),
                )
            ]
        )
        return id
