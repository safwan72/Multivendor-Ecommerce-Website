from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy

def customer():
    def decorator(view_fun):
        def wrap(request,*args,**kwargs):
                if request.user.is_customer or request.user.is_staff:
                    return view_fun(request,*args,**kwargs)
                else:
                    return HttpResponseRedirect(reverse_lazy('App_Login:home'))
        return wrap 
    return decorator

def seller():
    def decorator(view_fun):
        def wrap(request,*args,**kwargs):
            try:
                if request.user.is_seller or request.user.is_staff:
                    return view_fun(request,*args,**kwargs)
                else:
                    return HttpResponseRedirect(reverse_lazy('App_Login:home'))
                    
            except PermissionError:
                return HttpResponseRedirect(reverse_lazy('App_Login:home'))
        return wrap 
    return decorator