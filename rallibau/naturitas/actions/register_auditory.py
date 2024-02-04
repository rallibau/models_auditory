from naturitas.domain.Auditory import Auditory
from naturitas.domain.auditory_repository import AuditoryRepository
from naturitas.domain.domain_object_updated import DomainObjectUpdated


class RegisterAuditory:
    def __init__(self, auditory_repo: AuditoryRepository):
        self.auditory_repo = auditory_repo

    def execute(self, event: DomainObjectUpdated) -> int:
        auditory: Auditory = Auditory(
            change_date=event.change_date,
            user=event.user,
            model_name=event.model_name,
            model_instance_id=event.model_instance_id,
            data_before_change=event.data_before_change,
            data_after_change=event.data_after_change,
        )
        return self.auditory_repo.save(auditory)
