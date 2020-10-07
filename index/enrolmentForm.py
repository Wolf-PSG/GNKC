from django import forms
from django.core.validators import RegexValidator

class DateInput(forms.DateInput):
    input_type ='date'

yesOrNoChoices = (
    ('1', 'Yes'),
    ('2', 'No'),
)

attendanceChoices = (
    ('1', 'Saturday AM'),
    ('2', 'Saturday PM'),
    ('3', 'Sunday AM'),
    ('4', 'Sunday PM'),
    ('5', 'Any')
)
class enrolmentForm(forms.Form):
    first_Name = forms.CharField(label='First Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    address = forms.CharField(label = 'Address', max_length=100)
    dob = forms.DateField(label='Date of Birth',widget=DateInput)
    telephoneNumber = forms.CharField(label='Telephone Number', max_length=11, validators=[RegexValidator(r'^\d{11}$')])
    email = forms.CharField(label='Email', max_length=100)
    sibling = forms.ChoiceField(label='Does any brother and sister attend this college?', choices = yesOrNoChoices)
    medical = forms.ChoiceField(label='Any medical or special needs?', required=False, choices = yesOrNoChoices)
    ifYesMedical = forms.CharField(label='if Yes, could you specify', required=False, max_length=100)
    fee = forms.ChoiceField(label='Have you already paid the Annual fee', choices = yesOrNoChoices)
    beginner = forms.ChoiceField(label='Are you starting from level 1 (beginner)', choices=yesOrNoChoices)
    attendance = forms.ChoiceField(label='Preferred Day and Time', choices=attendanceChoices)
    schoolPermission = forms.ChoiceField(label='Do you give the College permission to take pictures/videos of your child for promotional and educational purposes?', choices=yesOrNoChoices) 
    termsRead = forms.ChoiceField(label='Have you read the terms and conditions?', required=True,choices=yesOrNoChoices)