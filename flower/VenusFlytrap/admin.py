from django.contrib import admin

# Register your models here.
from VenusFlytrap.models import Test, korisnik, answer


class TestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Test, TestAdmin)


class korisnikAdmin(admin.ModelAdmin):
    pass


admin.site.register(korisnik, korisnikAdmin)


class answerAdmin(admin.ModelAdmin):
    pass


admin.site.register(answer, answerAdmin)
