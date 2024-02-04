from django.contrib.auth.models import Group, User
from rest_framework import serializers

from naturitas.models import ModelOne, AuditoryModel, ModelTwo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class OneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelOne
        fields = [
            "id",
            "field_1",
            "field_2",
            "field_2",
            "field_3",
            "field_4",
            "field_5",
            "field_6",
            "field_7",
            "field_8",
            "field_9",
            "field_10",
            "field_11",
            "field_12",
            "field_13",
            "field_14",
            "field_15",
        ]


class TwoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModelTwo
        fields = [
            "id",
            "field_1",
            "field_2",
            "field_2",
            "field_3",
            "field_4",
            "field_5",
            "field_6",
            "field_7",
            "field_8",
            "field_9",
            "field_10",
            "field_11",
            "field_12",
            "field_13",
            "field_14",
            "field_15",
        ]


class AuditorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuditoryModel
        fields = [
            "date",
            "user",
            "model",
            "model_instance_id",
            "data_before_change",
            "data_after_change",
        ]
