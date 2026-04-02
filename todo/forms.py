from django import forms

from todo.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
        }


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.prefetch_related("tasks__tags"),
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input"}),
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
        }


class TagUpdateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
