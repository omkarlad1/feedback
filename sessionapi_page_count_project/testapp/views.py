from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=request.session.get('count',0)
    new_count=count+1
    request.session['count']=new_count
    #print('age:',request.seesion.get_expiry_age())
    #print('date:',request.session.get_expiry_date())
    #request.sessions.set_expiry(120)
    return render(request,'testapp/count.html',{'count':count})
