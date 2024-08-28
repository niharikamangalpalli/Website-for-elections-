from django.shortcuts import render,HttpResponse
from datetime import datetime
from votingapp.models import contact
from django.contrib import messages
def bjpinfo(request):
    return render(request,'votingapp/bjp.html')
def conginfo(request):
    return render(request,'votingapp/cong.html')
def info(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        vote=request.POST.get('vote')
        if name and email and phone and vote:  # Basic validation
            try:
                cont = contact(name=name, email=email, phone=phone, vote=vote, date=datetime.today())
                cont.save()
                messages.success(request,"Your vote has been successfully submitted")
                return render(request, 'votingapp/inform.html')
            
            except Exception as e:
                # Handle the exception (e.g., log it, show an error message)
                return HttpResponse("Error while saving data."+ f'{name},{email},{phone},{vote},{e}')
        else:
            return HttpResponse("Please fill in all fields."+ f'{name},{email},{phone},{vote}')


    return render(request,'votingapp/inform.html')