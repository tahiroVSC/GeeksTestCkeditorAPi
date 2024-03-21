from apps.trainer.models import Trainer, Type_of_trainer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.trainer.serializers import TrainerSerializer, Type_of_trainerSerializer


class Type_of_trainerViewAPI(ListAPIView):
    queryset = Type_of_trainer.objects.all()
    serializer_class = Type_of_trainerSerializer


class Type_of_trainerDetailViewAPI(RetrieveAPIView):
    queryset = Type_of_trainer.objects.all()
    serializer_class = Type_of_trainerSerializer
    lookup_field = 'id'


class TrainerViewAPI(ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerDetailViewAPI(RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    lookup_field = 'id'
