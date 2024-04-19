from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from .models import Appointment

class DatePickerForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["service", "date"]
        widgets = {
            'service': forms.Select(attrs={'class': 'form-select', 'dir':"auto", "style" : "font-family: 'Vazir';", 'onchange':"checkService()"}),
        }

    def __init__(self,*args,**kwargs):
        super(DatePickerForm,self).__init__(*args,**kwargs)
        self.fields['date'] = JalaliDateField(label="تاریخ نوبت", widget=AdminJalaliDateWidget)
        self.fields['date'].widget.attrs.update({
            'class': 'jalali_date-date',
            "style" : "font-family: 'Vazir';",
            'onchange':"checkService()",
            "readonly":"readonly",
        })

    