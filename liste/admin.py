from django.contrib import admin


from liste.models import Band, Annonce

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste 


class AnnonceAdmin(admin.ModelAdmin): 
    list_display = ('titre','band','description', 'year', 'type')

admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(Band, BandAdmin)