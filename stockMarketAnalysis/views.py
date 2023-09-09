from datetime import datetime, timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.shortcuts import redirect, render
from rest_framework import viewsets
from .serializers import entity_serializer
from .models import stock_market_data
from .forms import addnew_form
import json


def home(request):
    entities = stock_market_data.objects.all().order_by('date')
    paginator = Paginator(entities, 10)
    page_number = request.GET.get('page')
    entity = paginator.get_page(page_number)
    total_pages=entity.paginator.num_pages
    data ={
        'entity':entity,
        # 'page_list':[n+1 for n in range(total_pages)]
        'total_pages':total_pages
    }
    return render(request,"index.html",data)

#Update Action Form
def update(request,entity_id):
    entity=stock_market_data.objects.get(pk=entity_id)
    return render(request,"update.html/",{'entity':entity})

#Saving updated data to database
def do_update(request,entity_id):
    try:
        if request.method=="POST":
            trade_code =request.POST.get("trade_code")
            high =request.POST.get("high")
            low = request.POST.get("low")
            open_value = request.POST.get("open")
            close =request.POST.get("close")
            volume =request.POST.get("volume")
        
            entity=stock_market_data.objects.get(pk=entity_id)
            entity.trade_code =trade_code
            entity.high =high
            entity.low = low
            entity.open=open_value
            entity.close =close
            entity.volume =volume
            entity.save()
            return redirect("/")
    except Exception as e:
        messege = f'Please insert a Correct value: {e}'
        return HttpResponseServerError(messege)

#Delete Action
def delete_entity(request,entity_id):
    entity=stock_market_data.objects.get(pk=entity_id)
    entity.delete()
    return redirect("/")


#New data inserting form
def insert(request):
    form = addnew_form()
    return render(request,"addnew.html",{'form':form})

#Saving new data to database
def save_data(request):
    try:
        if request.method=="POST":
            # date = request.POST.get("date")
            trade_code =request.POST.get("trade_code")
            high =request.POST.get("high")
            low = request.POST.get("low")
            open_value = request.POST.get("open")
            close =request.POST.get("close")
            volume =request.POST.get("volume")
        
            posting_date = datetime.now()
            date= posting_date.date()
        
            entity=stock_market_data(date=date,trade_code=trade_code,high=high,low=low,open=open_value,close=close,volume=volume)
            entity.save()
        return redirect("/")    
    except Exception as e:
        messege=f"Please insert a valid type:{e}"    
        return HttpResponseServerError(messege)

#Options for add, upload json file and delete_all
def options(request):
    if request.method=='POST':
        x=request.POST.get("option")
        if x== 'add':
            return redirect("/insert/")
        elif x=="delete":
            return redirect("/deleteAll/")
        else:
            return redirect("/jsonForm/")
        
#To delete all the data
def deleteAll(request):
    entities = stock_market_data.objects.all()
    entities.delete()
    return redirect("/")

#uploading json file form
def jsonform(request):
    return render(request,"json_form.html/",{})

#Saving json file to database
def loadJSON(request):
    if request.method == 'POST':
        if 'json_file' in request.FILES:
            uploaded_file = request.FILES['json_file']
            try:
                data_from_json = json.load(uploaded_file)
                for x in data_from_json:
                    date = x["date"]
                    trade_code = x["trade_code"]
                    high = x["high"]
                    low = x["low"]
                    open_value = x["open"]
                    close = x["close"]
                    volume = x["volume"]
                    entity = stock_market_data(date=date, trade_code=trade_code, high=high, low=low, open=open_value, close=close, volume=volume)
                    entity.save()
                return JsonResponse({'message': 'File uploaded successfully'})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data in the uploaded file'}, status=400)
        else:
            return JsonResponse({'error': 'Please Upload A JSON File'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


#Data exchange through api
class stockMarketViewSet(viewsets.ModelViewSet):
    queryset= stock_market_data.objects.all()
    serializer_class=entity_serializer
