from naturitas.domain.two import Two
from naturitas.domain.two_repository import TwoRepository
from naturitas.models import ModelTwo


class DjangoTwoRepository(TwoRepository):
    def get(self, id: int) -> Two:
        one = ModelTwo.objects.get(pk=id)
        return self._to_domain(one)

    def save(self, instance_of_two: Two) -> int:
        model_one = ModelTwo.objects.create(
            field_1=instance_of_two.field_1,
            field_2=instance_of_two.field_2,
            field_3=instance_of_two.field_3,
            field_4=instance_of_two.field_4,
            field_5=instance_of_two.field_5,
            field_6=instance_of_two.field_6,
            field_7=instance_of_two.field_7,
            field_8=instance_of_two.field_8,
            field_9=instance_of_two.field_9,
            field_10=instance_of_two.field_10,
            field_11=instance_of_two.field_11,
            field_12=instance_of_two.field_12,
            field_13=instance_of_two.field_13,
            field_14=instance_of_two.field_14,
            field_15=instance_of_two.field_15,
        )
        return model_one.id

    def _to_domain(self, one):
        return Two(
            id=one.id,
            field_1=one.field_1,
            field_2=one.field_2,
            field_3=one.field_3,
            field_4=one.field_4,
            field_5=one.field_5,
            field_6=one.field_6,
            field_7=one.field_7,
            field_8=one.field_8,
            field_9=one.field_9,
            field_10=one.field_10,
            field_11=one.field_11,
            field_12=one.field_12,
            field_13=one.field_13,
            field_14=one.field_14,
            field_15=one.field_15,
        )
