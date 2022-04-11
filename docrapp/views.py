from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("Hello, world. You're at the docrapp index.")


def doctor(request):
    dummy_response = {
        "id": 2,
        "full_name": "John Doe",
        "age": 30,
        "blood_type": "AB+ve",
        "history": [
            {
                "date": "23 January 2022",
                "diagnosis": "Diabetes",
                "prescription": [
                    {
                        "name": "Metformin HydroChloride",
                        "dosage": "100mg",
                        "routine": "1-0-1",
                        "duration": "2 weeks"
                    },
                    {
                        "name": "Atorvastatin",
                        "dosage": "100mg",
                        "routine": "1-1-1",
                        "duration": "2 weeks"
                    },
                    {
                        "name": "Paracetamol",
                        "dosage": "100mg",
                        "routine": "1-1-1",
                        "duration": "2 weeks"
                    }
                ]
            }
        ]
    }

    return JsonResponse(dummy_response)
