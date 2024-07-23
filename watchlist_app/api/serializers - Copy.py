from rest_framework import serializers
from watchlist_app.models import Movie

def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("name is too short!!!")
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.name)
        instance.active = validated_data.get('active',instance.name)
        instance.save()
        return instance
    
    def validate(self, data):
        """
        Check that description and name should not be equ.
        """
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description should not be equal")
        return data
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name should be at least 2 characters long.")
    #     return value