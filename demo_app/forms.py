from django import forms


class EditWorksiteForm(forms.Form):
    """ Add New Worksite Form """
    name = forms.CharField(max_length=150, label='Name')
    shift = forms.ChoiceField(choices=[(x, x) for x in range(1, 13)], label='Shift Timing (AM/ PM)')
    buffer_time = forms.TimeField(widget=forms.TimeInput(
        format='%M'), label='Start Buffer time for reports (Minutes)', input_formats=['%M', ])
    cutoff_time = forms.TimeField(widget=forms.TimeInput(format='%M'),
                                  label='Patrol start cut-off time (Minutes)', input_formats=['%M', ])
    contact_no = forms.CharField(max_length=12, label='Contact Number (+65)')
    address = forms.CharField(widget=forms.Textarea)
    device = forms.CharField(max_length=255, label='Device IMEI / IMEI1 Number')

    def __init__(self, *args, **kwargs):
        super(EditWorksiteForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        # field.widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control   '
