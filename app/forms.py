from django import forms
from app.models import *
class TopicForm(forms.Form):
    topic_name = forms.CharField()

tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
class WebpageForm(forms.Form):
    topic_name = forms.ChoiceField(choices=tl)
    name = forms.CharField()
    url = forms.URLField()

wl=[[wo.pk,wo.name] for wo in Webpage.objects.all()]
class AccessRecordForms(forms.Form):
    name = forms.ChoiceField(choices=wl)
    date = forms.DateField()
    author = forms.CharField()

class DeptForm(forms.Form):
    deptno = forms.IntegerField()
    dname = forms.CharField(max_length = 100)
    loc = forms.CharField(max_length = 100)

dl=[[do.deptno,do.deptno] for do in Dept.objects.all()]
class EmployeeForm(forms.Form):
    empno = forms.IntegerField()
    ename = forms.CharField()
    job = forms.CharField()
    mgr =  forms.IntegerField()
    hiredate = forms.DateField()
    sal = forms.IntegerField()
    comm = forms.IntegerField()
    deptno = forms.ChoiceField(choices=dl)
