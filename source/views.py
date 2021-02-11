from django.shortcuts import render, redirect
from .forms import PersonDetailsForm, PrayerDetailsForm, ScheduledDateForm
from .models import PersonDetails, PrayerDetails, ScheduleDate
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'Prayer/index.html')


@login_required
def index2(request):
    if request.method == 'POST':
        form = PersonDetailsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            location = form.cleaned_data.get('location')
            age = form.cleaned_data.get('age')
            request.session['name'] = name
            person = PersonDetails(
                name=name,
                location=location,
                age=age
            )
            person.save()
            return redirect('source:index3')
    else:
        form = PersonDetailsForm()
    context = {
        'form': form
    }
    return render(request, 'Prayer/page2.html', context)


@login_required
def index3(request):
    name = request.session.get('name')
    context = {
        'name': name
    }
    return render(request, 'Prayer/page3.html', context)


@login_required
def index4(request):
    if request.method == 'POST':
        form = PrayerDetailsForm(request.POST)
        if form.is_valid():
            prayer = form.cleaned_data.get('prayer')
            person_prayer = PrayerDetails(
                prayer=prayer
            )
            person_prayer.save()
            return redirect('source:index5')
    else:
        form = PrayerDetailsForm()
    context = {
        'form': form
    }
    return render(request, 'Prayer/page4.html', context)


@login_required
def index5(request):
    name = request.session.get('name')
    context = {
        'name': name
    }
    return render(request, 'Prayer/page5.html', context)


@login_required
def index6(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        request.session['price'] = price
        return redirect('source:payment')
        return redirect('source:index8')
    return render(request, 'Prayer/page6.html')


@login_required
def index7(request):
    price = request.session.get('price')
    context = {
        'price': price
    }
    return render(request, 'Prayer/payment.html', context)


@login_required
def index8(request):
    if request.method == 'POST':
        form = ScheduledDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            email = form.cleaned_data.get('email')
            sch_date = ScheduleDate(
                date=date,
                email=email
            )
            sch_date.save()
            name = request.session.get('name')
            sendmail(request, email, name)
            return redirect('source:payment')
    else:
        form = ScheduledDateForm()
    context = {
        'form': form
    }
    return render(request, 'Prayer/page7.html', context)



def sendmail(request, email, name):
    name = request.session.get('name')
    template = render_to_string('Prayer/email.html', {'name': name})
    emailed = EmailMessage(
        'The Prayer Partners',
        template,
        settings.EMAIL_HOST_USER,
        [email]
    )
    emailed.fail_silently = False
    emailed.send()


@login_required
def index9(request):
    return render(request, 'Prayer/page8.html')