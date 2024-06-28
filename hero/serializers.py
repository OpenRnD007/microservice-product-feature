from rest_framework import serializers
from hero.models import Titles

class TitlesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Titles model.

    Converts complex data types, such as querysets and model instances, to 
    Python data types that can then be easily rendered into JSON, XML, or other content types.
    """
    class Meta:
        """
        Meta class to map serializer's fields with the model fields.
        """
        model=Titles 
        fields=('tconst','titleType','primaryTitle','originalTitle','isAdult','startYear','endYear','runtimeMinutes','genres')
        
        # Specifies the fields to be included in the serialized output