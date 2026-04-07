from django import forms
from .models import Showtime, Seat

class BookingForm(forms.Form):
    showtime = forms.ModelChoiceField(
        queryset=Showtime.objects.none(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    seats = forms.ModelMultipleChoiceField(
        queryset=Seat.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'seat-checkbox'}),
        required=True
    )

    def __init__(self, *args, **kwargs):
        movie = kwargs.pop('movie', None)
        super(BookingForm, self).__init__(*args, **kwargs)
        
        if movie:
            self.fields['showtime'].queryset = Showtime.objects.filter(movie=movie)
            
            # Get the initial showtime from the form data or initial data
            showtime = None
            if 'showtime' in self.data:
                try:
                    showtime = Showtime.objects.get(id=self.data['showtime'])
                except (Showtime.DoesNotExist, ValueError):
                    pass
            elif 'showtime' in self.initial:
                showtime = self.initial['showtime']
            
            if showtime:
                self.fields['seats'].queryset = Seat.objects.filter(
                    theater=showtime.theater,
                    status='available'
                ) 