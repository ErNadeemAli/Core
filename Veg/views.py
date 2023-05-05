from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.db.models import Q, Sum
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    if request.method == 'POST':
        res_name = request.POST.get('receipe_name')
        res_desc = request.POST.get('receipe_desc')
        res_image = request.POST.get('receipe_image')
        print(res_image)
        
        obj = Receipe(receipe_name=res_name,
                      receipe_desc=res_desc, receipe_image=res_image)
        obj.save()
        return HttpResponseRedirect('/veg')

    res = Receipe.objects.all()

    return render(request, 'home.html', {'res': res})


def get_student(request):

    queryset = Student.objects.all()
    data = {'data': queryset}

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = Student.objects.filter(
            Q(student_name__icontains=search) |
            Q(student_email__icontains=search) |
            Q(student_age__icontains=search) |
            Q(student_id__student_id__icontains=search) |
            Q(department__department_name__icontains=search)
        )

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    # print(page_obj)

    data = {'queryset': page_obj}
    return render(request, 'student.html', context=data)


def check_marks(request, studentid):
    queryset = SubjectMarks.objects.filter(
        student__student_id__student_id=studentid)

    total_mark = queryset.aggregate(total_mark=Sum('marks'))
    total = len(queryset)*100
    current_rank = -1
    ranks = Student.objects.annotate(
        marks=Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    i = 1
   
   
    for rank in ranks:

        
        if studentid == rank.student_id.student_id:
            current_rank = i

            break
        i = i+1

    return render(request, 'marks.html', {'queryset': queryset, 'total_marks': total_mark, 'total': total, 'current_rank': current_rank})
def get_top(request):
    current_rank = -1
    ranks = Student.objects.annotate(
        marks=Sum('studentmarks__marks')).order_by('-marks', 'student_age')
    i = 1
   
   
    for rank in ranks:

        studentid=Student.objects.all()
        if studentid == rank.student_id.student_id:
            current_rank = i

           
        i = i+1

    return render(request, 'top.html',{'ranks':ranks,'currnt_rank':current_rank})