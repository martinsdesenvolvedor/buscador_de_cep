from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def busca_cep(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    
    elif request.method == 'POST':
        cep = request.POST.get('cep')

        url = f'https://viacep.com.br/ws/{cep}/json/'
        requisicao = requests.get(url)

        if requisicao.status_code == 200:
            requisicao_dic = requisicao.json()
            print(requisicao_dic)

            if 'cep' in requisicao_dic:
                cep = requisicao_dic['cep']
                logradouro = requisicao_dic['logradouro']
                bairro = requisicao_dic['bairro']
                cidade = requisicao_dic['localidade']
                estado = requisicao_dic['uf']
                return render(request, 'cep.html', {'cep': cep, 'logradouro': logradouro, 'bairro': bairro, 'cidade': cidade, 'estado': estado})
        
            
            else:
                return HttpResponse('Cep não Encontrado ou Inválido!')
               
            

        else:
            return HttpResponse(f'Erro na requisição!, {requisicao.status_code}')


