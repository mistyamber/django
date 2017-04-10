from django.views import View
from django.shortcuts import render


#def hello_world(request):
    #print(request.GET)
    #return HttpResponse('Hello World')

class HelloWorldView(View):
    def get(self, request):
	    response = render(request, 'hello_world.html', {})
	    return response