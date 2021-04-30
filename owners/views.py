import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db import Error
from owners.models import Owners, Dogs


class OwnersView(View):
    def get(self, request):
        owner_queryset = Owners.objects.all()
        owner_list = [o.to_dict() for o in owner_queryset]

        return JsonResponse({"results": owner_list}, status=200)


class DogsView(View):
    def get(self, request):
        dog_queryset = Dogs.objects.all()
        dog_list = [d.to_dict() for d in dog_queryset]

        return JsonResponse({"results": dog_list}, status=200)


def createOwner(request):

    if request.method != "POST":
        return JsonResponse({"Error": "Use POST method instead."}, status=405)

    required_keys = ["name", "email", "age"]
    req = json.loads(request.body)

    # Check if required info satisfied
    for key in required_keys:
        if key not in req.keys():
            return JsonResponse({"message": "Not Enough Information."})

    # Data create attempt
    data = {k: v for k, v in req.items() if k in required_keys}
    try:
        owner = Owners.objects.create(**data)
    except Error as e:
        return JsonResponse({"error": repr(e.__cause__)}, status=500)
    else:
        return JsonResponse({"message": "Success", "item": owner.to_dict()}, status=201)


def createDog(request):
    if request.method != "POST":
        return JsonResponse({"Error": "Use POST method instead."}, status=405)

    required_keys = ["owner_id", "name", "age"]
    req = json.loads(request.body)

    # Check if required info satisfied
    for key in required_keys:
        if key not in req.keys():
            return JsonResponse({"message": "Not Enough Information."})

    # Data create attempt
    data = {k: v for k, v in req.items() if k in required_keys}
    try:
        owner_id = data.pop("owner_id")
        owner = Owners.objects.get(id=owner_id)
        dog = Dogs.objects.create(owner=owner, **data)

    except Error as e:
        return JsonResponse({"error": repr(e.__cause__)}, status=500)
    else:
        return JsonResponse({"message": "Success", "item": dog.to_dict()}, status=201)
