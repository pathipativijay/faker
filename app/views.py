
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()

    d={'ts':topics}
    return render(request,'display_topic_name.html',d)



def display_webpage(request):
    webpages=webpage.objects.all()
    #webpages=webpage.objects.filter(topic_name='Foot Ball')
    #webpages=webpage.objects.exclude(topic_name='Foot Ball')
    #webpages=webpage.objects.all()[0:2:]
    #webpages=webpage.objects.all()[-3]
    #webpages=webpage.objects.all().order_by('name')
    #webpages=webpage.objects.all().order_by('-name')
    #webpages=webpage.objects.all().order_by(Length('name'))
    #webpages=webpage.objects.all().order_by(Length('name').desc())
    #webpages=webpage.objects.filter(name__startswith='Jes')
    #webpages=webpage.objects.filter(name__endswith='l')
    #webpages=webpage.objects.filter(name__contains='t')
    #webpages=webpage.objects.filter(name__in=('Stacy','Tony'))
    #webpages=webpage.objects.filter(name__regex=r'^[a-zA-Z]{2}r')
    #webpages=webpage.objects.filter(Q(topic_name='Foot Ball') & Q(name='Carol'))
    #webpages=webpage.objects.filter(Q(topic_name='Foot Ball') & Q(url__startswith='https') & Q(name__endswith='n'))

    d={'ws':webpages}
    return render(request,'display_webpage.html',d)

def display_access(request):
    #access=Accessrecord.objects.all()
    #access=Accessrecord.objects.filter(date='1990-03-30')
    #access=Accessrecord.objects.filter(date__gte='1990-03-30')
    #access=Accessrecord.objects.filter(date__lt='1990-03-30')
    #access=Accessrecord.objects.filter(date__year='2000')
    #access=Accessrecord.objects.filter(date__year__gt='2000')
    #access=Accessrecord.objects.filter(date__month='11')
    #access=Accessrecord.objects.filter(date__day='9')

    d={'ac':access}
    return render(request,'display_access.html',d)


