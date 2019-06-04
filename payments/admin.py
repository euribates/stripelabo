from django.contrib import admin

# Register your models here.


from .models import StripIntent 


class StripIntentAdmin(admin.ModelAdmin):
    class meta:
        model = StripIntent
    pass


admin.site.register(StripIntent, StripIntentAdmin)
