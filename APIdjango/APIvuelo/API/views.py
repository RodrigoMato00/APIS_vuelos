from django.shortcuts import render
from django.views import View
from .models import Vuelo
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.

class VueloListView(View):
    def get(self, request):
         if ('name' in request.GET):
             vlist = Vuelo.objects.filter(name__contains=request.GET['name'])
             #/api/vuelo/?name=

             return JsonResponse(list(vlist.values()), safe=False)

         else:
            vlist = Vuelo.objects.all()
            #/api/vuelo/

            return JsonResponse(list(vlist.values()), safe=False)


class VueloDetailView(View):
    def get(self, request, pk):
        vuelodetail = Vuelo.objects.get(pk=pk)
        return JsonResponse(model_to_dict(vuelodetail))