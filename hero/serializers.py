from rest_framework import serializers
from hero.models import Titles

class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Titles 
        fields=('tconst','titleType','primaryTitle','originalTitle','isAdult','startYear','endYear','runtimeMinutes','genres')