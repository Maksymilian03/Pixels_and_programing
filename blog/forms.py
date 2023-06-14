from datetime import date

from django.core.exceptions import ValidationError
from django.forms import (
    CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, ModelForm, ImageField
)

from .models import Article


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class ArticleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Article
        fields = '__all__'

    title = CharField(validators=[capitalized_validator])
    contents = CharField()
    date = DateField()
    jpg = ImageField()

