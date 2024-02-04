from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class One:
    field_1: datetime
    field_2: datetime
    field_3: str
    field_4: float
    field_5: bool
    field_6: bool
    field_7: bool
    field_8: bool
    field_9: bool
    field_10: bool
    field_11: bool
    field_12: bool
    field_13: bool
    field_14: bool
    field_15: bool
    id: int = None

    def to_json(self):
        return {
            "field_1": self.field_1.strftime("%Y-%m-%d %H:%M:%S"),
            "field_2": self.field_2.strftime("%Y-%m-%d %H:%M:%S"),
            "field_3": self.field_3,
            "field_4": self.field_4,
            "field_5": self.field_5,
            "field_6": self.field_6,
            "field_7": self.field_7,
            "field_8": self.field_8,
            "field_9": self.field_9,
            "field_10": self.field_10,
            "field_11": self.field_11,
            "field_12": self.field_12,
            "field_13": self.field_13,
            "field_14": self.field_14,
            "field_15": self.field_15,
        }

