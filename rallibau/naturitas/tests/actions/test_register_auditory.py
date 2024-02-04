from naturitas.actions.register_auditory import RegisterAuditory
from naturitas.domain.Auditory import Auditory
from naturitas.domain.auditory_repository import AuditoryRepository
from naturitas.tests.domain.auditory_factory import AuditoryFactory

RANDOM_NEW_INSTANCE_ID = 2


class InMemoryAuditoryRepository(AuditoryRepository):
    def save(self, auditory: Auditory) -> int:
        return RANDOM_NEW_INSTANCE_ID


class TestRegisterAuditory:
    def test_register_auditory_should_save_auditory_instance(self):
        auditory_instance = AuditoryFactory.build()
        result = RegisterAuditory(auditory_repo=InMemoryAuditoryRepository()).execute(
            auditory_instance
        )

        assert result == RANDOM_NEW_INSTANCE_ID
