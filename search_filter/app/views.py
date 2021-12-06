from django.shortcuts import render
from .models import EmpModel
# Create your views here.
def search_filter(request):
    if request.method=='POST':
        gender=request.POST.get('gender')
        occupation=request.POST.get('occupation')
        print('gender ',gender)
        print('occupation ',occupation)
        emp_objif=EmpModel.objects.raw('select *from employee where gender="'+gender+'" and occupation="'+occupation+'"')
        return render(request,'index.html',{'emp':emp_objif})
    else:
        emp_obj=EmpModel.objects.raw('select *from employee')
        return render(request,'index.html',{'emp':emp_obj})


