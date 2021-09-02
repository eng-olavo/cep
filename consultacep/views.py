from django.shortcuts import render

def consultacep(request):
    if request.POST:
        cep = request.POST.get('cep')


        return render(request,'consultacep.html')
