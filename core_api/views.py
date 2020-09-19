from django.shortcuts import render
from .serializers import AccountSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.db import models


class API(APIView):

    def get(self, request):


        if self.request.query_params.get('email', None) :
            email = self.request.query_params.get('email', None)
            if email:
                if User.objects.filter(username= email).exists():
                    user = User.objects.filter(username= email)
                    if user[0]:
                        id = user[0].id
                        if user[0]:
                            data = {
                                'user_id': id,
                                'login_type': 'signin',
                            }
                            return Response(data)
                else:
                    data = {
                        'user_id': 'not registered',
                        'login_type': 'signup',
                    }
                    return Response(data)

        if self.request.query_params.get('userid', None) and self.request.query_params.get('password', None):
            userId = self.request.query_params.get('userid', None)
            password = self.request.query_params.get('password', None)

            if User.objects.filter(id= userId, password= password).exists():
                user = User.objects.filter(id= userId, password= password)

                if user[0]:
                    data = {
                        'message' : "login successful"
                    }
                    return Response(data)
            else:
                data = {
                    'message':"failed"
                }
                return Response(data)
        
        
            



    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data= request.data)
                



        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
