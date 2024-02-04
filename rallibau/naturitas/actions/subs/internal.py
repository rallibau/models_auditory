from naturitas.actions.register_auditory import RegisterAuditory
from naturitas.domain.domain_object_updated import DomainObjectUpdated
from naturitas.domain.events import EventSubscriber
from naturitas.infrastructure.django_auditory_repository import DjangoAuditoryRepository


class DomainObjectUpdatedSub(EventSubscriber[DomainObjectUpdated]):
    def on(self, event: DomainObjectUpdated) -> None:
        RegisterAuditory(auditory_repo=DjangoAuditoryRepository()).execute(event)
