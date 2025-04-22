from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'cardanim':True}
    return render(request, 'pages/index.html', context=context)