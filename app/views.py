from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO = TopicForm()
    d={'topics':ETFO}

    if request.method == 'POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is Created')
        else:
            return HttpResponse('Data is invalid')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO = WebpageForm()
    d={'webpages':EWFO}

    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            n=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=ur)[0]
            WO.save()
            return HttpResponse('Webpage is Created')
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EARFO = AccessRecordForms()
    d={'accessrecords':EARFO}

    if request.method == 'POST':
        ARFDO=AccessRecordForms(request.POST)
        if ARFDO.is_valid():
            na=ARFDO.cleaned_data['name']
            da=ARFDO.cleaned_data['date']
            auth=ARFDO.cleaned_data['author']
            WO=Webpage.objects.get(pk=na)
            ARO=AccessRecord.objects.get_or_create(name=WO,date=da,author=auth)[0]
            ARO.save()
            return HttpResponse('AccessRecord is Successfully Created.....')
        else:
            return HttpResponse('Data is invalid')
    return render(request,'insert_accessrecord.html',d)

def insert_dept(request):
    EDFO=DeptForm()
    d={'dept':EDFO}

    if request.method == 'POST':
        DFDO=DeptForm(request.POST)
        if DFDO.is_valid():
            deptnum=DFDO.cleaned_data['deptno']
            deptname=DFDO.cleaned_data['dname']
            deptloc=DFDO.cleaned_data['loc']
            DO=Dept.objects.get_or_create(deptno=deptnum,dname=deptname,loc=deptloc)[0]
            DO.save()
            return HttpResponse('Dept is Created')
        else:
            return HttpResponse('Data is Invalid')
    return render(request,'insert_dept.html',d)

def insert_employee(request):
    EEFO=EmployeeForm()
    d={'employees':EEFO}

    if request.method == 'POST':
        EFDO=EmployeeForm(request.POST)
        if EFDO.is_valid():
            empnum=EFDO.cleaned_data['empno']
            empname=EFDO.cleaned_data['ename']
            empjob=EFDO.cleaned_data['job']
            empmgr=EFDO.cleaned_data['mgr']
            hdate=EFDO.cleaned_data['hiredate']
            empsal=EFDO.cleaned_data['sal']
            empcomm=EFDO.cleaned_data['comm']
            deptnum=EFDO.cleaned_data['deptno']
            DO=Dept.objects.get(deptno=deptnum)
            EO=Employee.objects.get_or_create(empno=empnum,ename=empname,job=empjob,mgr=empmgr,hiredate=hdate,sal=empsal,comm=empcomm,deptno=DO)[0]
            EO.save()
            return HttpResponse('Employee is Created...')
        else:
            return HttpResponse('Data is invalid')
    return render(request,'insert_employee.html',d)
