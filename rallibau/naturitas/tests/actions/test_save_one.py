from datetime import datetime
from typing import Generator
from unittest.mock import Mock, create_autospec

import pytest
from freezegun import freeze_time

from naturitas.actions.save_one import SaveOne
from naturitas.domain.domain_object_updated import DomainObjectUpdated
from naturitas.domain.one import One
from naturitas.domain.one_repository import OneRepository
from naturitas.domain.publishers import InternalEventPublisher
from naturitas.tests.domain.one_factory import OneFactory

RANDOM_NEW_INSTANCE_ID = 2


class InMemoryOneRepository(OneRepository):
    memory = {}

    def get(self, id: int) -> One:
        return self.memory[id]

    def save(self, instance_of_one: One) -> int:
        self.memory[instance_of_one.id] = instance_of_one
        return RANDOM_NEW_INSTANCE_ID


@pytest.fixture
def mock_internal_publisher() -> Generator[Mock, None, None]:
    yield create_autospec(spec=InternalEventPublisher, spec_set=True, instance=True)


@freeze_time("2024-02-03T11:23:40+02:00")
class TestOneSaver:
    def test_one_saver_should_insert_one_instance(self, mock_internal_publisher):
        repo = InMemoryOneRepository()
        one_instance = OneFactory.build(id=None)
        result = SaveOne(
            one_repo=repo, internal_event_publisher=mock_internal_publisher
        ).execute(one=one_instance, user="random_user")

        event = DomainObjectUpdated(
            change_date=datetime(2024, 2, 3, 9, 23, 40),
            user="random_user",
            model_name="one",
            model_instance_id=RANDOM_NEW_INSTANCE_ID,
            data_before_change={},
            data_after_change={
                "field_1": "2024-02-03 11:23:40",
                "field_2": "2024-02-03 11:23:40",
                "field_3": "random",
                "field_4": 22.22,
                "field_5": True,
                "field_6": True,
                "field_7": True,
                "field_8": True,
                "field_9": True,
                "field_10": True,
                "field_11": True,
                "field_12": True,
                "field_13": True,
                "field_14": True,
                "field_15": True,
            },
        )
        mock_internal_publisher.publish.assert_called_once_with([event])

        assert result == RANDOM_NEW_INSTANCE_ID

    def test_one_saver_should_update_instance(self, mock_internal_publisher):
        repo = InMemoryOneRepository()
        one_instance = OneFactory.build(id=1, field_5=False)
        repo.save(one_instance)
        update_instance = OneFactory.build(id=1, field_5=True)

        SaveOne(
            one_repo=repo, internal_event_publisher=mock_internal_publisher
        ).execute(one=update_instance, user="random_user")

        event = DomainObjectUpdated(
            change_date=datetime(2024, 2, 3, 9, 23, 40),
            user="random_user",
            model_name="one",
            model_instance_id=RANDOM_NEW_INSTANCE_ID,
            data_before_change={
                "field_1": "2024-02-03 11:23:40",
                "field_2": "2024-02-03 11:23:40",
                "field_3": "random",
                "field_4": 22.22,
                "field_5": False,
                "field_6": True,
                "field_7": True,
                "field_8": True,
                "field_9": True,
                "field_10": True,
                "field_11": True,
                "field_12": True,
                "field_13": True,
                "field_14": True,
                "field_15": True,
            },
            data_after_change={
                "field_1": "2024-02-03 11:23:40",
                "field_2": "2024-02-03 11:23:40",
                "field_3": "random",
                "field_4": 22.22,
                "field_5": True,
                "field_6": True,
                "field_7": True,
                "field_8": True,
                "field_9": True,
                "field_10": True,
                "field_11": True,
                "field_12": True,
                "field_13": True,
                "field_14": True,
                "field_15": True,
            },
        )
        mock_internal_publisher.publish.assert_called_once_with([event])
