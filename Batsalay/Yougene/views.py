from django.http import HttpResponse

def index(request, name, surname, age, hobby):
    first = f'<h1> My name - {name}, my surname - {surname}. </h1>'\
            f'<h2>Im {age} old </h2>'\
            f'<h2>my hobby is {hobby}</h2>'
    return HttpResponse(first)

def about(request, place, grades, like):
    about = f'<h1> im from {place}.</h1>' \
            f'<h2> my grades are {grades}.</h2>' \
            f'<h2> i like {like} </h2>'
    return HttpResponse(about)

def contacts(request, git, tel):
    contacts = f'<h1> my github - {git}</h1>' \
               f'<h2> my telegram - {tel}</h2>'

    return HttpResponse(contacts)