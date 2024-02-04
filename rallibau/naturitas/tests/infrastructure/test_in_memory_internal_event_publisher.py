from datetime import datetime
from typing import Generator
from unittest.mock import Mock, patch

import pytest

from naturitas.actions.register_auditory import RegisterAuditory
from naturitas.domain.domain_object_updated import DomainObjectUpdated
from naturitas.infrastructure.in_memory_internal_event_publisher import (
    InMemoryInternalEventPublisher,
)


class TestInMemoryInternalEventPublisher:
    @pytest.fixture
    def mock_auditory_action(self) -> Generator[Mock, None, None]:
        with patch.object(RegisterAuditory, "execute") as mock:
            yield mock

    def test_calls_register_auditory_on_domain_object_updated(
        self, mock_auditory_action: Mock
    ) -> None:
        event_publisher = InMemoryInternalEventPublisher()

        event = DomainObjectUpdated(
            change_date=datetime.now(),
            user="foo",
            model_name="one",
            data_before_change={},
            data_after_change={},
            model_instance_id=1,
        )
        event_publisher.publish([event])

        mock_auditory_action.assert_called_once_with(event)
