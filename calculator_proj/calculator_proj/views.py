from django.http import HttpResponse

def add(request, num1, num2):
    sum = num1 + num2
    html = f"<html><body>The result of {num1} + {num2} is {sum}</body></html>"
    return HttpResponse(html)

def subtract(request, num1, num2):
    diff = num1 - num2
    html = f"<html><body>The result of {num1} - {num2} is {diff}</body></html>"
    return HttpResponse(html)