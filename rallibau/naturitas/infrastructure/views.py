from datetime import datetime

from django.contrib.auth.models import Group, User
from requests import Request
from rest_framework import permissions, status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from naturitas.actions.save_one import SaveOne
from naturitas.actions.save_two import SaveTwo
from naturitas.domain.one import One
from naturitas.domain.two import Two
from naturitas.infrastructure.django_one_repository import DjangoOneRepository
from naturitas.infrastructure.django_two_repository import DjangoTwoRepository
from naturitas.infrastructure.in_memory_internal_event_publisher import InMemoryInternalEventPublisher
from naturitas.infrastructure.serializers import AuditorySerializer, GroupSerializer, OneSerializer, TwoSerializer, \
    UserSerializer
from naturitas.models import AuditoryModel, ModelOne, ModelTwo


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HealthView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request, *args: list, **kwargs: dict) -> Response:
        return Response(status=status.HTTP_200_OK, data={})


class OneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ModelOne.objects.all()
    serializer_class = OneSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        one_instance = One(
            field_1=datetime.fromisoformat(request.data["field_1"]),
            field_2=datetime.fromisoformat(request.data["field_2"]),
            field_3=request.data["field_3"],
            field_4=request.data["field_4"],
            field_5=_get_boolean_request_param(request, "field_5"),
            field_6=_get_boolean_request_param(request, "field_6"),
            field_7=_get_boolean_request_param(request, "field_7"),
            field_8=_get_boolean_request_param(request, "field_8"),
            field_9=_get_boolean_request_param(request, "field_9"),
            field_10=_get_boolean_request_param(request, "field_10"),
            field_11=_get_boolean_request_param(request, "field_11"),
            field_12=_get_boolean_request_param(request, "field_12"),
            field_13=_get_boolean_request_param(request, "field_13"),
            field_14=_get_boolean_request_param(request, "field_14"),
            field_15=_get_boolean_request_param(request, "field_15"),
        )
        SaveOne(
            one_repo=DjangoOneRepository(), internal_event_publisher=InMemoryInternalEventPublisher()).execute(
            one=one_instance,
            user=request.user
        )
        return super().list(request, *args, **kwargs)


def _get_boolean_request_param(request, key: str):
    value = request.data.get(key, False)
    if value == "true":
        return True
    return False


class TwoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ModelTwo.objects.all()
    serializer_class = TwoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        two_instance = Two(
            field_1=datetime.fromisoformat(request.data["field_1"]),
            field_2=datetime.fromisoformat(request.data["field_2"]),
            field_3=request.data["field_3"],
            field_4=request.data["field_4"],
            field_5=_get_boolean_request_param(request, "field_5"),
            field_6=_get_boolean_request_param(request, "field_6"),
            field_7=_get_boolean_request_param(request, "field_7"),
            field_8=_get_boolean_request_param(request, "field_8"),
            field_9=_get_boolean_request_param(request, "field_9"),
            field_10=_get_boolean_request_param(request, "field_10"),
            field_11=_get_boolean_request_param(request, "field_11"),
            field_12=_get_boolean_request_param(request, "field_12"),
            field_13=_get_boolean_request_param(request, "field_13"),
            field_14=_get_boolean_request_param(request, "field_14"),
            field_15=_get_boolean_request_param(request, "field_15"),
        )
        SaveTwo(
            two_repo=DjangoTwoRepository(), internal_event_publisher=InMemoryInternalEventPublisher()).execute(
            two=two_instance,
            user=request.user
        )
        return super().list(request, *args, **kwargs)


class AuditoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AuditoryModel.objects.all()
    serializer_class = AuditorySerializer
    permission_classes = [permissions.IsAuthenticated]
