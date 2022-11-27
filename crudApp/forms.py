from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    task = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"id": "todofield", "placeholder": "Input your todo here"}
        ),
    )

    class Meta:
        model = Todo
        fields = ["task"]
