from django import forms
from user.personal_info.models import PersonalInfo


class PersonalInfoForm(forms.ModelForm):
     class Meta:
          model = PersonalInfo
          fields = '__all__'