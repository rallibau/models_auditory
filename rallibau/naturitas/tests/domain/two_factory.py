from datetime import datetime

from factory import DictFactory

from naturitas.domain.two import Two


class TwoFactory(DictFactory):
    field_1 = datetime(2024, 2, 3, 11, 23, 40)
    field_2 = datetime(2024, 2, 3, 11, 23, 40)
    field_3 = "random"
    field_4 = 22.22
    field_5 = True
    field_6 = True
    field_7 = True
    field_8 = True
    field_9 = True
    field_10 = True
    field_11 = True
    field_12 = True
    field_13 = True
    field_14 = True
    field_15 = True

    class Meta:
        model = Two
