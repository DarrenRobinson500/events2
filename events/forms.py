from django import forms
from django.forms import ModelForm
from .models import Tree, Answer

class TreeForm(ModelForm):
    class Meta:
        model = Tree
        fields = ('question', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'result1', 'result2', 'result3', 'result4', 'result5', )
        labels = {
            'number':'number',
            'name':'name',
            'temp':'temp',
            'notes':'notes',
            'question':'Question',
            'answer1':'Answer1',
            'answer2':'Answer2',
            'answer3':'Answer3',
            'answer4':'Answer4',
            'answer5':'Answer5',
            'result1':'Result1',
            'result2':'Result2',
            'result3':'Result3',
            'result4':'Result4',
            'result5':'Result5',
        }
        widgets = {
            'number': forms.TextInput(attrs={'class':'form-control','placeholder':'number'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
            'notes': forms.Textarea(attrs={'class':'form-control','placeholder':'notes'}),
            'question': forms.TextInput(attrs={'class':'form-control','placeholder':'question'}),
            'answer1': forms.TextInput(attrs={'class':'form-control','placeholder':'answer1'}),
            'answer2': forms.TextInput(attrs={'class':'form-control','placeholder':'answer2'}),
            'answer3': forms.TextInput(attrs={'class':'form-control','placeholder':'answer3'}),
            'answer4': forms.TextInput(attrs={'class':'form-control','placeholder':'answer4'}),
            'answer5': forms.TextInput(attrs={'class':'form-control','placeholder':'answer5'}),
            'result1': forms.TextInput(attrs={'class':'form-control','placeholder':'result1'}),
            'result2': forms.TextInput(attrs={'class':'form-control','placeholder':'result2'}),
            'result3': forms.TextInput(attrs={'class':'form-control','placeholder':'result3'}),
            'result4': forms.TextInput(attrs={'class':'form-control','placeholder':'result4'}),
            'result5': forms.TextInput(attrs={'class':'form-control','placeholder':'result5'}),
        }

class AnswerStatusForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('information','ho_review','ho_reg_affairs_review','quality','reported')
        labels = {
            'email_code': 'Latest email type sent',
            'information': 'Information is complete',
            'ho_review': 'Reviewed by relevant Head Of',
            'ho_reg_affairs_review': 'Reviewed by Head Of Regulatory Affairs',
            'quality': 'Quality as assessed by Head Of Regulatory Affairs'
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('name', 'date_identified', 'nature', 'description', 'why_reportable', 'how_identified',
                  'duration','representative_details', 'how_rectified', 'remediation', 'future_compliance',
                  'quality')
          #        'quality', 'ho_reg_affairs_comments')
        labels = {
            'name': 'Name of event:',
            'date_arose':'Date of the reportable situation',
            'date_identified':'Date the reportable situation was identified',
            'nature':'Nature of the reportable situation',
            'description': "Description of reportable situation",
            'why_reportable':'Why the breach is significant',
            'how_identified':'How was the reportable situation identified',
            'duration':'How long did the breach last (include whether the breach is continuing)',
            'representative_details':'Information about representatives',
            'how_rectified':'Whether and how the reportable situation has been rectified',
            'remediation':'Whether and when affected clients have been compensated',
            'future_compliance':'Future compliance - steps to ensure future compliance',
            'ho_reg_affairs_comments': 'Head of Regulatory Affairs Comments',
            'quality': 'Head of Regulatory Affairs Approval',
        }
        widgets = {
            'date_arose': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'date_identified': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'name': forms.Textarea(attrs={'class':'form-control','placeholder':'name','rows':4}),
            'nature': forms.Textarea(attrs={'class':'form-control','placeholder':'nature','rows':4}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'nature','rows':4}),
            'why_reportable': forms.Textarea(attrs={'class':'form-control','placeholder':'why reportable','rows':4}),
            'how_identified': forms.Textarea(attrs={'class':'form-control','placeholder':'how identified','rows':4}),
            'duration': forms.Textarea(attrs={'class':'form-control','placeholder':'duration','rows':4}),
            'representative_details': forms.Textarea(attrs={'class':'form-control','placeholder':'The reportable situation relates to a deemed significant breach','rows':4}),
            'how_rectified': forms.Textarea(attrs={'class':'form-control','placeholder':'How rectified','rows':4}),
            'remediation': forms.Textarea(attrs={'class':'form-control','placeholder':'Remediation','rows':4}),
            'future_compliance': forms.Textarea(attrs={'class':'form-control','placeholder':'Future compliance','rows':4}),
            'ho_reg_affairs_comments': forms.Textarea(attrs={'class':'form-control','placeholder':'Comments','rows':4}),
        }