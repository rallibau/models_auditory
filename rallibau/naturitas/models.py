from django.db import models


class ModelOne(models.Model):
    field_1 = models.DateField()
    field_2 = models.DateField(null=True)
    field_3 = models.TextField()
    field_4 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    field_5 = models.BooleanField()
    field_6 = models.BooleanField()
    field_7 = models.BooleanField()
    field_8 = models.BooleanField()
    field_9 = models.BooleanField()
    field_10 = models.BooleanField()
    field_11 = models.BooleanField()
    field_12 = models.BooleanField()
    field_13 = models.BooleanField()
    field_14 = models.BooleanField()
    field_15 = models.BooleanField()

    class Meta:
        db_table = "model_one"


class ModelTwo(models.Model):
    field_1 = models.DateField()
    field_2 = models.DateField(null=True)
    field_3 = models.TextField()
    field_4 = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    field_5 = models.BooleanField()
    field_6 = models.BooleanField()
    field_7 = models.BooleanField()
    field_8 = models.BooleanField()
    field_9 = models.BooleanField()
    field_10 = models.BooleanField()
    field_11 = models.BooleanField()
    field_12 = models.BooleanField()
    field_13 = models.BooleanField()
    field_14 = models.BooleanField()
    field_15 = models.BooleanField()

    class Meta:
        db_table = "model_two"


class AuditoryModel(models.Model):
    date = models.DateField()
    user = models.TextField()
    model = models.TextField()
    model_instance_id = models.IntegerField()
    data_before_change = models.JSONField()
    data_after_change = models.JSONField()

    class Meta:
        db_table = "auditory_model"
