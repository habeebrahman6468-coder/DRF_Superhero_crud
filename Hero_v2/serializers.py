from rest_framework import serializers

class SuperheroSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()

    gender = serializers.CharField()

    powers = serializers.CharField()

    universe = serializers.CharField()

