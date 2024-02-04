import pytest

from naturitas.infrastructure.django_one_repository import DjangoOneRepository
from naturitas.models import ModelOne
from naturitas.tests.domain.one_factory import OneFactory


@pytest.mark.django_db(transaction=True)
class TestDjangoOneRepository:
    def test_repository_should_save_object(self):
        one_instance = OneFactory.build()
        DjangoOneRepository().save(one_instance)
        assert ModelOne.objects.filter(field_3="random").exists()

    def test_repository_should_update_object(self):
        one_instance = OneFactory.build(id=None, field_5=True)
        id = DjangoOneRepository().save(one_instance)
        one_instance_updated = OneFactory.build(id=id, field_5=False)
        DjangoOneRepository().save(one_instance_updated)

        assert ModelOne.objects.filter(id=id, field_5=False).exists()

    def test_repository_should_return_object(self):
        one_instance = OneFactory.build()
        id = DjangoOneRepository().save(one_instance)

        returned_object = DjangoOneRepository().get(id=id)
        assert returned_object.id == id
