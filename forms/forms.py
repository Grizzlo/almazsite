from django import forms
from .models import BookingTourModel,BookingModel

class BookingTourForm(forms.ModelForm):

    class Meta:
        model = BookingTourModel
        fields = ('username','tel_user_phone','user_email','date_entry','tour_name','number_of_people','user_comment')

class BookingForm(forms.ModelForm):

    class Meta:
        model = BookingModel
        fields = ('username','tel_user_phone','user_email','hotel','room_class','date_entry','date_out','number_of_people','user_comment')
