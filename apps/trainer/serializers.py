from rest_framework import serializers
from apps.trainer.models import Trainer, Type_of_trainer


class Type_of_trainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_of_trainer
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    type_of_trainer_ru = serializers.ReadOnlyField(source='type_of_trainer.name_ru')
    type_of_trainer_ky = serializers.ReadOnlyField(source='type_of_trainer.name_ky')
    
    class Meta:
        model = Trainer
        exclude = ('name', 'description', 'type_of_trainer')

