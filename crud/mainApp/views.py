from urllib.request import Request
from django.shortcuts import redirect, render
from django.db.models import  Q
from .models import Employee


def homes(Request):
    if (Request.method == "POST"):
        search = Request.POST.get("search")
        data = Employee.objects.filter(
            Q(name__icontains=search)|
            Q(email__icontains=search)|
            Q(state__icontains=search)|
            Q(city__icontains=search))
    else:
        data = Employee.objects.all()
    return render(Request, "indexc.html", {'data': data})


def delete(Request, id):
    data = Employee.objects.get(id=id)
    if (data):
        data.delete()
    return redirect("/")


def addRecord(Request):
    if (Request.method == "POST"):
        e = Employee()
        e.name = Request.POST.get("name")
        e.email = Request.POST.get("email")
        e.phone = Request.POST.get("phone")
        e.salary = Request.POST.get("salary")
        e.city = Request.POST.get("city")
        e.state = Request.POST.get("state")
        e.save()
        return redirect("/")
    return render(Request, "add.html")


def updateRecord(Request, id):
    data = Employee.objects.get(id=id)
    if (Request.method == "POST"):
        data.name = Request.POST.get("name")
        data.email = Request.POST.get("email")
        data.phone = Request.POST.get("phone")
        data.salary = Request.POST.get("salary")
        data.city = Request.POST.get("city")
        data.state = Request.POST.get("state")
        data.save()
        return redirect("/")
    return render(Request, "update.html", {"data": data})
