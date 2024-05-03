from django.shortcuts import render,get_object_or_404,redirect
from .forms import customUsercretionForm,managerceationForm,docterceationForm,employerceationForm,branchrceationForm,patientceationForm
from .models import branch,doctor,manager,employer,patient


from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpRequest
from .forms import loginform


def manager_dashbord(request,branch_id):
    branch=branch.objects.all(id=branch_id)
    doctors=branch.manager.all()
    employers=branch.employer.all()
    patients=branch.patient.all()
    return render(request,'manager.html',{'brnchs':branch,'docters':doctors,'patient':patient})

    #profile
    #creat docter(crud)
    #creat employers crud
    #listof pationt and the pationt description crud
    #the pationt qotsor deta list
    
    pass
    
    
    



def docter_dashbord():
    #profile
    #listof pationt and the pationt description
    return HttpRequest('docter')
    


    


def employer_dashbord(request):
    #the pationt qotsor deta list,input field 
    #profile
    #listof pationt and the pationt description
    #crud of patient
    return HttpRequest('employer')
    



def patient_dashbord(request):
    return HttpRequest('patient')
    



    #login form


def login_view(request):
    if request.method == 'post':
        form=loginform(request.post)
        if form.is_valid():
            username=request.post.get('username')
            password=request.post.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                if user.is_manager:
                    return redirect('manager_dashbord')
                elif user.is_docter:
                    return redirect('docter_dashbord')
                elif user.is_employer:
                    return redirect('employer_dashbord')
                else:
                    return redirect('patient_dashbord')
            else:
                messages.error(request,'invalid user')
    else:
        form=loginform()
    return render(request,'login.html',{'form':form})
    
                







   #creation of the branch

def creat_branch(request):
    if request.mothed == 'post':
        form=branchrceationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
        
    else:
        form=branchrceationForm()

    return render(request,'creat_branch.html',{'form':form})


def creat_manager(request,branch_id):
    branch=get_object_or_404(branch,pk=branch_id)
    if request.mothed == 'post':
        form=managerceationForm(request.post)
        if form.is_valid():
            manager=form.save(commit=False)
            manager.branch=branch
            manager.save()
            
            return redirect('manager_dashbord',branch_id=branch_id)
        
    else:
        form=managerceationForm()

    return render(request,'creat_branch.html',{'form':form ,'branch':branch})





def creat_docter(request,branch_id):
    branch=get_object_or_404(branch,pk=branch_id)
    if request.method == 'post':
        form=docterceationForm(request.post)
        if form.is_valid():
            docter=form.save(commit=False)
            docter.branch=branch
            docter.save()
            
            return redirect('docter_dashbord',branch_id=branch_id)
            
    else:
        form=docterceationForm()
    return render(request,'docter.html',{'form':form ,'branch':branch})

def creat_employer(request):
    if request.method == 'post':
        form=employerceationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('employer_list')
        
    else:
        form=employerceationForm()

    return render(request,'creat_employer.html',{'form':form})


def creat_patient(request):
    if request.mothed == 'post':
        form=patientceationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
        
    else:
        form=patientceationForm()

    return render(request,'creat_patient.html',{'form':form})


def creat_cusemuser(request):
    if request.mothed == 'post':
        form=customUsercretionForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('custem_list')
        
    else:
        form=customUsercretionForm()

    return render(request,'coutem.html',{'form':form})



#docterslist
def docters_list(request):
    pass

#delete docter
def delete_dector(request,branch_id):
    docter=get_object_or_404(doctor,id=branch_id)
    docter.delete()
    return render('manager_dashbord')

# Create your views here.
