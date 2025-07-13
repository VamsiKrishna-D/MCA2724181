from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(request):
    template = get_template('pdf_template.html')
    html = template.render({'title': 'My PDF', 'message': 'Hello from Django PDF'})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
