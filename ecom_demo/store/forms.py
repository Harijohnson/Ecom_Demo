from django import forms
from store.models import user_info


class add_studen(forms.ModelForm):
    class Meta:
        model=user_info
        fields='__all__'