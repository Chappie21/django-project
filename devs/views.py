from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.
class HelloWorld(View):
    
    def get(self, request):
        # return HttpResponse(status=200, content="Hola mundo desde Django")

        data = {
            'name': 'Andres Chaparro',
            'years': 23,
            'skills': [
                'React',
                'Angular',
                'Django',
                'Express',
                'FastAPI'
            ]   
        }

        return render(request=request, template_name='hello_world.html', context=data)