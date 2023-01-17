from django.shortcuts import render
def home(request):
    data=dict()
    import datetime
    data['time']=datetime.date.today()
    # data['xy']=xy
    return render(request,"home.html",context=data)
# Create your views here.
