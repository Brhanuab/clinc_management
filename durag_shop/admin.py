from django.contrib import admin
from .models import CustomUser,manager,doctor,employer,patient,branch


admin.site.register(CustomUser)
admin.site.register(branch)
admin.site.register(manager)
admin.site.register(doctor)
admin.site.register(employer)
admin.site.register(patient)


# Register your models here.
