from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fullText = request.GET['fullText']
    print(fullText)
    
    txtlst = fullText.split()

    txtDic = {}

    for word in txtlst:
        if word in txtDic:
            txtDic[word] += 1
        else:
            txtDic[word] = 1

    sorted_x = sorted(txtDic.items(), key = operator.itemgetter(1),reverse=True)
    print(sorted(txtDic))
    return render(request,"count.html",{'fullText':fullText, 'countOfWords': len(txtlst) ,'countOfLetters':len(fullText),'sortedDic':sorted_x})

def aboutUs(request):
    return render(request,"about.html")
    