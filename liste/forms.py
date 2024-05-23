from django import forms
from liste.models import Band, Annonce


class ContactUsForm(forms.Form):
    Nom = forms.CharField(required=False)
    email = forms.CharField()
    message = forms.CharField(max_length=1000)

# Laissez votre modèle définir la forme
# class BandForm(forms.Form):
#    name = forms.CharField(max_length=100)
#    biography = forms.CharField(max_length=1000)
#    year_formed = forms.IntegerField(min_value=1900, max_value=2021)
#    official_homepage = forms.URLField(required=False)

class BandForm(forms.ModelForm): #Générez automatiquement un formulaire à partir d'un modèle avec un ModelForm
   class Meta:
     model = Band
    #  fields = '__all__'
     exclude = ('active', 'official_homepage') 


class AnnonceForm(forms.ModelForm):
   class Meta:
     model = Annonce
     fields = '__all__'