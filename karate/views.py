from django.shortcuts import render


def json_fields(request):
    return render(request, 'karate/json_fields.html')
