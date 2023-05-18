from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WantedPerson
from .serializers import WantedPersonSerializer
from .scraping.web_scraper import scrape_fbi_website #, scrape_interpol_website

class WantedPersonListView(APIView):
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
    def get(self, request, pk):
        wanted_person = WantedPerson.objects.get(pk=pk)
        serializer = WantedPersonSerializer(wanted_person)
        return Response(serializer.data)
