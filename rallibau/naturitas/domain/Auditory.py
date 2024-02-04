from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Auditory:
    change_date: datetime
    user: str
    model_name: str
    model_instance_id: int
    data_before_change: dict
    data_after_change: dict
