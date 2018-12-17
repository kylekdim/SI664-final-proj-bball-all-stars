from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from allstars.models import PersonRecord


class PersonForm(forms.ModelForm):
	class Meta:
		model = PersonRecord
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit', 'Submit'))


class SearchForm(forms.ModelForm):
	height = forms.IntegerField(
		label='height',
		required=False
	)

	class Meta:
		model = PersonRecord
		fields = ['height']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'GET'
		self.helper.add_input(Submit('submit', 'Search'))