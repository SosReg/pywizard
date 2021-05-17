from django.shortcuts import render
import re
import pyautogui as ms
import random as rd
import time

# Create your views here.

def index(request):
    return render(request, 'webapps/appshome.html')


def resumematch(request):
    return render(request, 'webapps/resumematch.html')

def submit(request):
    try:
        a = ((re.sub(r'[^\w\s]', '', request.GET['user_resume'])).lower()).split()
        b = ((re.sub(r'[^\w\s]', '', request.GET['job_description'])).lower()).split()
        common_words = list(set(a).intersection(set(b)))
        missing_words = list(set(b) - set(a))
        matchPercentage = len(common_words) / (len(common_words) + len(missing_words)) * 100
        common_words = ', '.join(common_words)
        missing_words = ', '.join(missing_words)
        # self.result3 = "Match percentage: " + str(matchPercentage)

        posts = [
            {
                'missing_words': missing_words
            },
            {
                'matchPercentage': matchPercentage
            }
        ]
        context = {
            'posts': posts
        }
        return render(request, "webapps/resumematch_result.html", context)
    except ZeroDivisionError:
        e = ['Please make sure both fields are filled.']
        context = {'posts': e}
        return render(request, "webapps/resumematch_error.html", context)

def run(request):
    while True:
        ms.click()
        time.sleep(20)
##    for i in range(1,100):
##        ms.moveRel(rd.randint(-10,10),rd.randint(-10,10))
        
    return render(request, 'home/home.html')
