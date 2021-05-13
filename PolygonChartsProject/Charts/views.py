from .tasks import add_data
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import HistoricalDataSerializer
from .models import HistoricalData
from datetime import datetime
from django.shortcuts import render
import requests
from django.http import StreamingHttpResponse
from django.http import JsonResponse



api_key='JpFv6iSXMq69mzKD3YQ_M2XR68yMrVyg'

def datarequest(request):

    if request.method == 'POST':
        print('hi hi hi')
        start=datetime.strptime(request.POST['start'], '%Y-%m-%d')
        end = datetime.strptime(request.POST['end'], '%Y-%m-%d')
        ticker = request.POST['ticker']
        minutes = request.POST['ticker']

        query=str('https://api.polygon.io/v2/aggs/ticker/'+ str(ticker) +\
              '/range/1/minute/' + str(start.date()) + '/' + str(end.date()) +'?unadjusted=true&sort=asc&limit=5000&apiKey='\
              + api_key)
        response=requests.get(query)
        responseJson=response.json()
        dataFinal=[]
        for pre in responseJson['results']:

            dataFinal.append({"x": pre['t'], "y":[pre['o'], pre['h'], pre['l'], pre['c']]})


        add_data.s(dataFinal,ticker).apply_async()

        return JsonResponse(dataFinal, safe=False)
        #return data_2
    else:
        return StreamingHttpResponse("unsuccesful")




class HistoricalDataView(ListCreateAPIView):
    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer



class SingleHistoricalDataView(RetrieveUpdateDestroyAPIView):


    queryset = HistoricalData.objects.all()
    serializer_class = HistoricalDataSerializer


def home(request):
    return render(request, 'home.html')