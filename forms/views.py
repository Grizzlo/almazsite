from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.shortcuts import render_to_response
from django.utils import timezone
from django.utils.html import strip_tags
from django.core.mail import send_mail, EmailMultiAlternatives
from .forms import BookingForm, BookingTourForm
from django.utils.translation import gettext_lazy as _
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils import translation
from seo.models import SeoModel
# Create your views here.

booking_submission = _("Нове бронювання кімнати.Готель Алмаз")
tour_submission = _("Нове замовлення туру. Алмаз-тур")

def booking(request):
    page_id = 'Booking'
    page_seo_data = SeoModel.objects.get(page_name_en = page_id )
    lang = translation.get_language()
    if lang == 'en' :
        seo_title = page_seo_data.seo_title_en
        seo_description = page_seo_data.seo_description_en
        seo_keywords = page_seo_data.seo_keywords_en
    elif lang == 'ru' :
        seo_title = page_seo_data.seo_title_ru
        seo_description = page_seo_data.seo_description_ru
        seo_keywords = page_seo_data.seo_keywords_ru
    else:
        seo_title = page_seo_data.seo_title_uk
        seo_description = page_seo_data.seo_description_uk
        seo_keywords = page_seo_data.seo_keywords_uk

    if request.method == "POST":
        bookingForm = BookingForm(request.POST)
        if bookingForm.is_valid():
            book = bookingForm.save(commit=False)
            book.time = timezone.now()
            if book.hotel == 'Алмаз-плюс':
                html_content = render_to_string('book_template.html',{'username':book.username,'user_phone':book.tel_user_phone,'user_email':book.user_email,'hotel':_(book.hotel),'room_class':_(book.room_class),'date_entry':book.date_entry,'date_out':book.date_out,'number_of_people':book.number_of_people,'user_comment':book.user_comment,'booking_time':book.time})
                text_content = strip_tags(html_content)
                to_email = [book.user_email,]
                msg = EmailMultiAlternatives(booking_submission, text_content,'hotel.almaz.mail@gmail.com', to_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                translation.activate('uk')
                html_content = render_to_string('book_template.html',{'username':book.username,'user_phone':book.tel_user_phone,'user_email':book.user_email,'hotel':_(book.hotel),'room_class':_(book.room_class),'date_entry':book.date_entry,'date_out':book.date_out,'number_of_people':book.number_of_people,'user_comment':book.user_comment,'booking_time':book.time})
                text_content = strip_tags(html_content)
                to_email = ['hotel.almaz-plus@ukr.net',]
                msg = EmailMultiAlternatives(booking_submission, text_content,'hotel.almaz.mail@gmail.com', to_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                translation.activate(lang)
            else:
                html_content = render_to_string('book_template.html',{'username':book.username,'user_phone':book.tel_user_phone,'user_email':book.user_email,'hotel':_(book.hotel),'room_class':_(book.room_class),'date_entry':book.date_entry,'date_out':book.date_out,'number_of_people':book.number_of_people,'user_comment':book.user_comment,'booking_time':book.time})
                text_content = strip_tags(html_content)
                to_email = [book.user_email,]
                msg = EmailMultiAlternatives(booking_submission, text_content,'hotel.almaz.mail@gmail.com', to_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                translation.activate('uk')
                html_content = render_to_string('book_template.html',{'username':book.username,'user_phone':book.tel_user_phone,'user_email':book.user_email,'hotel':_(book.hotel),'room_class':_(book.room_class),'date_entry':book.date_entry,'date_out':book.date_out,'number_of_people':book.number_of_people,'user_comment':book.user_comment,'booking_time':book.time})
                text_content = strip_tags(html_content)
                to_email = ['administrator-almaz@rambler.ru',]
                msg = EmailMultiAlternatives(booking_submission, text_content,'hotel.almaz.mail@gmail.com', to_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                translation.activate(lang)
            #email.send()
            book.save()
            return redirect('redirect_booking')
    else:
        bookingForm = BookingForm()

    return render(request,'booking.html',{'booking':bookingForm, 'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})

def redirect_booking(request):
    return render(request, 'redirect_booking.html')

def redirect_tour(request):
    return render(request, 'redirect_tour.html')

def get_tour(request):
        if request.method == "POST":
            tourForm = BookingTourForm(request.POST)
            if tourForm.is_valid():
                tour = tourForm.save(commit=False)
                tour.time = timezone.now()


                html_content = render_to_string('tour_template.html',{'username':tour.username,'user_phone':tour.tel_user_phone,'user_email':tour.user_email,'date_entry': tour.date_entry,'tour_name': _(tour.tour_name),'number_of_people': tour.number_of_people,'user_comment': tour.user_comment,'tour_time':tour.time})
                text_content = strip_tags(html_content)
                to_email = [tour.user_email,]
                msg = EmailMultiAlternatives(tour_submission, text_content,'hotel.almaz.mail@gmail.com', to_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                translation.activate('uk')
                html_content = render_to_string('tour_template.html',{'username':tour.username,'user_phone':tour.tel_user_phone,'user_email':tour.user_email,'date_entry': tour.date_entry,'tour_name': _(tour.tour_name),'number_of_people': tour.number_of_people,'user_comment': tour.user_comment,'tour_time':tour.time})
                text_content = strip_tags(html_content)
                to_email = ['hotel.almaz@ukr.net']
                msg = EmailMultiAlternatives(tour_submission, text_content,'hotel.almaz.mail@gmail.com', to_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                translation.activate(lang)
                #content = template.render(context)
                tour.save()
                return redirect('redirect_tour')
        else:
            tourForm = BookingTourForm()
        return render(request, 'get_tour.html',{'tour':tourForm})
