from django.contrib import admin
from .models import Enquiry
# list_display=['title','unitprice']
# list_editable=['unitprice']
# list_per_page=10    #adding pagination
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    class Meta:
        model = Enquiry
        fields = '__all__'
        list_display = '__all__'

# admin.site.register(Enquiry)
#
# admin.site.register(Enquiry, EnquiryAdmin)


# Register your models here.
