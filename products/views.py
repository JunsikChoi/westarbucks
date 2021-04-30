from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


class ProductView(View):
    def get(self, request):
        return JsonResponse({"response": "Hello from ProductView!"}, status=200)
