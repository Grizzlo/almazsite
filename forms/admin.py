from django.contrib import admin
from .models import BookingTourModel,BookingModel
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('username','tel_user_phone','user_email','hotel','room_class','date_entry','date_out','number_of_people','user_comment','time')
    list_filter = ('username', 'hotel', 'date_entry')
    search_fields = ('name', 'email')

admin.site.register(BookingModel, BookingAdmin)


# Register your models here.
class BookingTourAdmin(admin.ModelAdmin):
    list_display = ('username','tel_user_phone','user_email','date_entry','tour_name','number_of_people','user_comment','time')
    list_filter = ('username', 'date_entry')
    #search_fields = ('name', 'email')
admin.site.register(BookingTourModel, BookingTourAdmin)
