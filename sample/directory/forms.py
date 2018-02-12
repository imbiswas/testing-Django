from django import forms
from directory.models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'