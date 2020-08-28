import django.forms as forms

class ContactForm(forms.Form):
    contact_full_name = form.CharField(max_length=100,required=True)
    contact_email = form.EmailField(required=True)
    contact_number = form.CharField(max_length=15,required=True)
    contact_company_name = forms.CharField(max_length=50,required=True)
    contact_description = forms.TextField(required=True)

class AppointmentForm(forms.Form):
    appointment_full_name = form.CharField(max_length=100,required=True)
    appointment_email = forms.EmailField(required=True)
    appointment_number = form.CharField(max_length=15,required=True)
    appointment_date = forms.DateField(required=True)
    appointment_time = form.TimeField(required=True,widget=forms.TimeInput(format='%H:%M',attrs={'placeholder':'Format HH/MM'}))
    appointment_description = forms.TextField(required=True)
