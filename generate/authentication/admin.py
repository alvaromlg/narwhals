from django.contrib import admin
from django.contrib.auth import get_user_model
from authemail.admin import EmailUserAdmin

class UserAdmin(EmailUserAdmin):
    list_display = ("email",
                    "date_of_birth",
                    "position",
                    "meters",
                    "minutes",
                    "strokes",
                    "metersAverage",
                    "minutesAverage",
                    "city_id",
                    "name",
                    "surname",
                    "trend")

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)
