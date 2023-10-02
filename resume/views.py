from django.shortcuts import render

# Create your views here.
def index(request) :
    context = {'name':'Mohammad Mahdi', 'lname':'Niknam', 'bio':'I am a student of Ali Bigdelis Django course and I just finished the fourth chapter. I follow this course through Maktabkhone website. I am interested in programming and I took the introductory and advanced Python course with Professor Jadi from Maktabkhone website and I also took the html and css course with Professor Mohammad Hossein Seyed Aghaei at Maktabkhone website.'}
    return render(request, 'index.html', context)