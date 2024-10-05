from django import forms
from userhome.models import UserPreference

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ['prefered_age_min', 'prefered_age_max', 'preferred_gender', 'education','location', 'interests_hobbies', 'relationship', 'height_min', 'height_max', 'weight_min', 'weight_max', 'lifestyle', 'religion', 'occupation']
    def __init__(self, *args, **kwargs):
        super(PreferenceForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True 
