from django.shortcuts import render


# Create your views here.
import subprocess


def home(request):
    return render(request, "scraping/index.html")

def scrape(request):
    
    process = subprocess.Popen(['python', 'manage.py', 'scrape'])
    return render(request, "scraping/index.html")

def summarize(request):
    
    process = subprocess.Popen(['python', 'manage.py', 'summarize'])
    return render(request, "scraping/index.html")

def tweet(request):
    
    process = subprocess.Popen(['python', 'manage.py', 'twitterbot'])
    return render(request, "scraping/index.html")




