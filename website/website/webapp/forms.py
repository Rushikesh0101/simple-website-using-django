from django import forms


class RegistrationForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    mobileno = forms.IntegerField()
    city = forms.CharField()
    pincode = forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea)

    def clean_mobileno(self):
        number = self.cleaned_data['mobileno']
        str_number = str(number)
        if len(str_number) == 10:
            return str_number
        else:
            raise forms.ValidationError("please enter a valid number")
