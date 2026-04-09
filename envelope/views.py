from django.shortcuts import render,redirect
from .forms import EnvelopeForm
from .models import Envelope

def envelopeForm(request):
    if request.method=='POST':
        form=EnvelopeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('todo')
    else:
        form=EnvelopeForm()
    return render(request,'envelope/form.html',{'form':form})
    
                