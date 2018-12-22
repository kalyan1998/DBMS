from django.contrib import admin

# Register your models here.
from .models import customer,bookings,accomodation,payment,payby,accomodationfor,transportationfor,transportation,package,eventsof,placeby,events,restaraunt,reserve,waterway,airway,roadway

admin.site.register(customer)
admin.site.register(bookings)
admin.site.register(accomodation)
admin.site.register(transportation)
admin.site.register(package)
admin.site.register(placeby)
admin.site.register(events)
admin.site.register(restaraunt)
admin.site.register(reserve)
admin.site.register(airway)
admin.site.register(roadway)
admin.site.register(waterway)
admin.site.register(eventsof)
admin.site.register(accomodationfor)
admin.site.register(transportationfor)
admin.site.register(payment)
admin.site.register(payby)