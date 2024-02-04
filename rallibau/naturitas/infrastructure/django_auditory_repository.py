from naturitas.domain.Auditory import Auditory
from naturitas.domain.auditory_repository import AuditoryRepository
from naturitas.models import AuditoryModel


class DjangoAuditoryRepository(AuditoryRepository):
    def save(self, auditory: Auditory) -> int:
        auditory_model = AuditoryModel.objects.create(
            date=auditory.change_date,
            user=auditory.user,
            model=auditory.model_name,
            model_instance_id=auditory.model_instance_id,
            data_before_change=auditory.data_before_change,
            data_after_change=auditory.data_after_change,
        )
        return auditory_model.id
