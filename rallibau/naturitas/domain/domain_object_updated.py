from dataclasses import dataclass
from datetime import datetime

from naturitas.domain.events import Event


@dataclass(frozen=True)
class DomainObjectUpdated(Event):
    change_date: datetime
    user: str
    model_name: str
    model_instance_id: int
    data_before_change: dict
    data_after_change: dict
