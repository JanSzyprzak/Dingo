from django import forms

class ResultForm(forms.Form):
   value = forms.FloatField(required=False)
   error = forms.CharField(required=False)

   def clean(self):
       cleaned_data = super().clean()
       value = cleaned_data.get('value')
       error = cleaned_data.get('error')

       if value and error:
           raise forms.ValidationError("Podaj tylko jedną z wartości")
       elif not (value or error):
           raise forms.ValidationError("Nie podano żadnej wartości!")