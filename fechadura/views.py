from django.shortcuts import render
from fechadura.models import Evento

# Create your views he
#def index(request):
    #return redirect('/agenda/')
def lista_eventos(request):
    
    evento  = Evento.objects.all()
    dados   = {'eventos': evento}
    return render(request, 'agenda.html', dados)

