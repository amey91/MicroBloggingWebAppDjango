from django import forms

from django.contrib.auth.models import User

from models import *

class CreateGrumbls(forms.Form):
    grumbl = forms.CharField(max_length = 250)
    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(CreateGrumbls, self).clean()
        grumbl=cleaned_data.get('grumbl')
        if not grumbl:
            raise forms.ValidationError("empty Grumbl detected.")
        # We must return the cleaned data we got from our parent.
        return cleaned_data



class GrumblrForm(forms.ModelForm):
    class Meta:
        model = Grumblr
        exclude=('user','dislikecounter')
        widgets={'picture' : forms.FileInput() }
        
class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(error_messages={'required': 'Please select a picture!'})
    class Meta:
        model = UserProfile
        exclude = ('user',)
        widgets = {'picture' : forms.FileInput() }
    
    