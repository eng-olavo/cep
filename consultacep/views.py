from django.shortcuts import render
import requests

def consultacep(request):

    dados_html = {}
    dados_cep = {}

    if request.POST:
        cep = request.POST.get('cep')
        url_cep = "https://viacep.com.br/ws/{}/json".format(cep)
        response = requests.get(url_cep)
        status_code = response.status_code
        dados_cep = response.json()

    return render(request,'consultacep.html', dados_cep)


