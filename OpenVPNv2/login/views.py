from django.shortcuts import render
# Create your views here.
from django.shortcuts import render_to_response,redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf

@csrf_protect
def login(request):
    print request.POST
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print 'USER=',username,'PASS=', password
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print 'authentificated'
            auth.login(request, user)
            return redirect('/home')
        else:
            print 'error'
            args['login_error'] = 'User was not found'
            return render_to_response('login.html',args)
    else:
        return render_to_response('login.html',args)

def logout(request):
    auth.logout(request)
    return redirect('/home')