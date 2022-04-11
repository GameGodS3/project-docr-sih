from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import shutil

from .ml.magic import voodoomagic

from .models import Patient
from PIL import Image
from io import StringIO



def home(request):
    return HttpResponse("Hello, world. You're at the docrapp index.")

@csrf_exempt
def patientSearch(request):
    if request.method == 'GET':

        patients = Patient.objects.all()

        found = False

        for patient in patients:
            print(patient.first_name)
            print(request.GET.get('name'))
            if patient.first_name == request.GET.get('name'):
                if str(patient.dob) == request.GET.get('dob'):
                    found = True
    if found:
        return JsonResponse({'status': 'found'})
    else:
        return JsonResponse({'status': 'notfound'})

@csrf_exempt
def getOCR(request):
    if request.method == 'POST':

        new_file = open('tmp/image.jpg', 'wb')
        i = request.FILES['image'].file
        shutil.copyfileobj(i, new_file)

        p_id = request.POST['id']

        # response =  voodoomagic()
        # ocr = response['value']

        ocr = 'nice'

    return JsonResponse({'ocr': ocr})


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
