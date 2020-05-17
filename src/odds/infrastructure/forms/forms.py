from django import forms
from .domain.models.bet import Bet


class SomeForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = '__all__'

    def save(self, commit=True):
        image = self.cleaned_data.pop('name')
        instance = super().save(commit=True)
        # instance.save_m2m()
        print(image)
        instance.image = image
        instance.save()
        return instance
