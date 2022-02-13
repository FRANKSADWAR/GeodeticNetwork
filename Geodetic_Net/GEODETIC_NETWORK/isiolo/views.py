from pipes import Template
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import logging
from isiolo.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from isiolo.models import County, Isiolo_Towns, StaffProfiles, Geodetic_Controls
from isiolo.forms import ReportIncidenceForm
import geojson
from django.views.generic import CreateView
from django.db.models import Count

logger = logging.getLogger(__name__)

@login_required
def home_page(request):
    data = Geodetic_Controls.objects.values('status').annotate(dcount=Count('status')).order_by()
    context = {
        'data':data,
    }
    return render(request,'index.html',context=context)




class ReportTemplate(LoginRequiredMixin,CreateView):
    template_name='reporting.html'
    login_url = '/login/'

    def get(self,request,*args,**kwargs):
        context = {'form':ReportIncidenceForm()}
        return render(request,'reporting.html',context)

    def post(self,request,*args,**kwargs):
        form = ReportIncidenceForm(request.POST)
        if form.is_valid():
            case = form.save()
            case.save()
            messages.success(request,'Station report has been received')
            return HttpResponseRedirect('/reporting/')
        else:
            messages.error(request,'Invalid form details, check geometry field')
        return render(request,'reporting.html',{'form':form})            


## LOGIN VIEWS ------------>>>>>
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    if user.is_staff:
                        login(request,user)
                        return HttpResponseRedirect('/admin/')
                    else:
                        login(request,user)
                        return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/deactivated/')
            else:
                messages.error(request,'Your credentials are incorrect, check again all the fields')
    else:
        login_form = LoginForm()
    return render(request,'registration/login.html',{'login_form':login_form})                

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/logout/')

def deactivate(request):
    return render(request,'registration/deactivated.html',{})

@csrf_protect
def register(request):
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            # set password as given by the user
            new_user.set_password(register_form.cleaned_data['password'])
            # Now save the User object
            new_user.save()

            # Also create a new profile instance associated with this user 
            StaffProfiles.objects.create(user=new_user)
            return render(request,'registration/register_done.html',{'new_user':new_user})
    else:
        register_form = UserRegistrationForm()
    return render(request,'registration/register.html',{'register_form':register_form})            

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST,instance=request.user)
        profile_form = ProfileEditForm(data=request.POST,files=request.FILES,instance=request.user.staffprofiles)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'User profile updated successfully')
        else:
            messages.error(request,'Error while updating profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.staffprofiles) 
    return render(request,'registration/edit_profile.html',{'user_form':user_form,'profile_form':profile_form})  

####### ------------- GEODATA VIEWS ------------

def towns_data(request):
    tw_data=serialize('geojson',Isiolo_Towns.objects.all())
    return HttpResponse(tw_data,content_type='json')

def isiolo(request):
    fence=County.objects.get(county='Isiolo')
    isiol=fence.geom.geojson
    return HttpResponse(isiol,content_type='json')

def geodetic_con(request):
    geod = serialize('geojson',Geodetic_Controls.objects.all())
    return HttpResponse(geod,content_type='json')

