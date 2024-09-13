# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'User registered successfully!')
            return redirect('login')
        else:
            for field, errors in serializer.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'registration.html', status=status.HTTP_400_BAD_REQUEST)
