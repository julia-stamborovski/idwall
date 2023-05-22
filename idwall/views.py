from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WantedPerson
from .serializers import WantedPersonSerializer
from .scraping.web_scraper import scrape_fbi_website #, scrape_interpol_website
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class WantedPersonListView(APIView):
    @swagger_auto_schema(
        operation_description="Obtém a lista de pessoas procuradas",
        responses={200: WantedPersonSerializer(many=True)},
    )
    def get(self, request):
        # Chama as funções de web scraping e obtém os dados coletados
        fbi_data = scrape_fbi_website()
        #interpol_data = scrape_interpol_website()

        # Serializa os dados do banco de dados
        wanted_persons = WantedPerson.objects.all()
        serializer = WantedPersonSerializer(wanted_persons, many=True)

        # Combina os dados do web scraping com os dados do banco de dados
        combined_data = serializer.data + fbi_data #+ interpol_data
        
        return Response(combined_data)

class WantedPersonDetailView(APIView):
    @swagger_auto_schema(
        produces=['application/json', 'application/xml'],
        operation_description="Obtém detalhes de uma pessoa procurada",
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description='ID da pessoa procurada',
                required=True,
            ),
        ],
        responses={200: WantedPersonSerializer()},
    )
    def get(self, request, pk):
        wanted_person = WantedPerson.objects.get(pk=pk)
        serializer = WantedPersonSerializer(wanted_person)
        return Response(serializer.data)

def home(request):
    return render(request, 'index.html')