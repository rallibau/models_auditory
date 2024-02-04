import pytest

from naturitas.infrastructure.django_two_repository import DjangoTwoRepository
from naturitas.models import ModelTwo
from naturitas.tests.domain.two_factory import TwoFactory


@pytest.mark.django_db(transaction=True)
class TestDjangoTwoRepository:
    def test_repository_should_save_object(self):
        two_instance = TwoFactory.build()
        DjangoTwoRepository().save(two_instance)
        assert ModelTwo.objects.filter(field_3="random").exists()

    def test_repository_should_return_object(self):
        two_instance = TwoFactory.build()
        id = DjangoTwoRepository().save(two_instance)

        returned_object = DjangoTwoRepository().get(id=id)
        assert returned_object.id == id
