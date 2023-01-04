import logging

from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import MessSerializer
from .serializers import PersonSerializer
import main
from .models import Person
import bcrypt
import json


def index(request):
    if not request.session.get('username'):
        return render(request, 'login.html')
    return render(request, 'index.html')

@api_view(['POST'])
def mess(request):
    if request.method == 'POST':  # user posting data
        data = {}
        data['user_name'] = request.session.get('username')
        data['message'] = request.POST.get('mess')
        serializer = MessSerializer(data=data)
        if serializer.is_valid():
            data = {'rMessage': main.chatbot_response(serializer.data.get("message"))}
            return JsonResponse(data)
        return redirect(index)

@api_view(['POST'])
def peopleLog(request):
    if request.method == 'POST':  # user posting data
        result = Person.objects.all()
        for object in result:
            if(object.username == request.POST.get('use')):
                if(bcrypt.checkpw(request.POST.get('pas').encode('utf-8'), object.password.encode('utf-8'))):
                    request.session["username"] = request.POST.get('use')
                    return redirect(index)
        return redirect(index)

@api_view(['POST'])
def peopleCreate(request):
    if request.method == 'POST':  # user posting data
        data = {}
        data['username'] = request.POST.get('user')
        data['password'] = bcrypt.hashpw(request.POST.get('password').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # save to db
            request.session["username"] = request.POST.get('user')
            return redirect(index)
        return redirect(index)

@api_view(['GET'])
def getPerson(request):
    if request.method == 'GET':  # user posting data
        if request.session.get('username'):
            data = {"get": request.session.get('username')}
            return JsonResponse(data)
        return redirect(index)

@api_view(['POST'])
def logOut(request):
    if request.method == 'POST':  # user posting data
        if request.session.get('username'):
            del request.session["username"]
            return redirect(index)
        return redirect(index)
