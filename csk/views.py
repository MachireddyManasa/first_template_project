from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name':'dhoni','age':'35'}
    return render(request,'jinja_print.html',context=d)