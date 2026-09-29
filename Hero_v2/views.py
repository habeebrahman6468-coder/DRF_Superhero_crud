from django.shortcuts import render

from rest_framework.views import APIView

from Hero.models import Superhero

from Hero_v2.serializers import SuperheroSerializer

from rest_framework.response import Response

# Create your views here.


class HeroListCreateView(APIView):

    def get(self,request):

        qs =Superhero.objects.all()

        serializer_instance =SuperheroSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = SuperheroSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            Superhero.objects.create(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)


class HeroRetrieveUpdateDeleteview(APIView):

    def get(self,request,pk=None):

        qs = Superhero.objects.get(id=pk)

        serializer_instance = SuperheroSerializer(qs)

        return Response(data=serializer_instance.data)
        







