from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
    template=get_template('index.html')
    variables=Context({})
    output = template.render(variables)
    return HttpResponse(output)
# Create your views here.
