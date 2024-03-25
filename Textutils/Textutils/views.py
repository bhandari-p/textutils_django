from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    # return HttpResponse("Home")
    return render (request,'index.html')

def analyze(request):
    # get the text
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')


# check box value
    if removepunc=="on":
        punctuations='''/?:;"',(){[}]_*^%$#@! '''
        analyzed=" "
        for char in djtext:
          if char not in punctuations:
              analyzed=analyzed+char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
         # analyze the text
        return render(request, 'analyze.html',params)
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to uppercase','analyzed_text':analyzed}    
        return render(request,'analyze.html',params )
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char != "\n":
             analyzed=analyzed+char
        params={'purpose':'New line Removed','analyzed_text':analyzed}    
        return render(request,'analyze.html',params )

    else:
        return HttpResponse("Error")



def about_us(request):
       return render(request,'about.html')