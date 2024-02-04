import pytest

from naturitas.infrastructure.django_auditory_repository import DjangoAuditoryRepository
from naturitas.models import AuditoryModel
from naturitas.tests.domain.auditory_factory import AuditoryFactory


@pytest.mark.django_db(transaction=True)
class TestDjangoAuditoryRepository:
    def test_repository_should_save_object(self):
        auditory_instance = AuditoryFactory.build(user="nobody@random.co")
        DjangoAuditoryRepository().save(auditory_instance)
        assert AuditoryModel.objects.filter(user="nobody@random.co").exists()
