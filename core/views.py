
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer


@csrf_exempt
def livro_list_create(request):
    
    '''verificacao metodo get HTTP'''
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)
    
    '''verificacao metodo post HTTP'''
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        
        '''validando se condiz com todos requisitos requiridos'''
        if serializer.is_valid():
            serializer.save()
            '''se validado correamente retornara o codigo de que foi completa a operacao'''
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        '''se houve algum erro retornara o codigo 400 como bedrequest'''
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def livro_detail(request, pk):
    livro = Livro.objects.get(pk=pk)
    
    '''metodo get passando o id do livro'''
    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)
    
    '''metodo put passando o id do livro'''
    if request.method == 'PUT':
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    '''metodo delete passando o id do livro'''
    if request.method == 'DELETE':
        livro.delete()
    '''se o livro for deletado retornara o codigo 204 confirmando'''
    return Response(status=status.HTTP_204_NO_CONTENT)

