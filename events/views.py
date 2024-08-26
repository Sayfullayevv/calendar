from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
import datetime
from .models import Venue

dt = datetime.datetime.now()

def home(request , year = dt.year , month = dt.strftime("%B")):
    month_number = list(calendar.month_name).index(month)
    month = month.capitalize()
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year , month_number)


    if request.method == 'POST':
        text = request.POST['text']
        post = Venue(text = text)
        post.save()
        obj = Venue.objects.all()

    return render(request , 'events/home.html' , {
        "cal": cal,
    })

