from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
import csv
from django.http import HttpResponse

def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect("home")
        else:
            messages.error(request, "There was an error, please try again")
            return redirect("home")
    else:
        return render(request, "home.html", {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home")

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # auth and log
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered and logged in")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "register.html", {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {'customer_record': customer_record})
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect("home")

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record has been deleted")
        return redirect("home")
    else:
        messages.error(request, "You must be logged in to delete a record")
        return redirect("home")
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been added")
                return redirect("home")
            else:
                messages.error(request, "There was an error adding the record")
        else:
            form = AddRecordForm()
            return render(request, "add_record.html", {'form': form})
    else:
        messages.error(request, "You must be logged in to add a record")
        return redirect("home")
    
def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record has been updated")
                return redirect("home")
            else:
                messages.error(request, "There was an error updating the record")
        return render(request, "update_record.html", {'form': form})
    else:
        messages.error(request, "You must be logged in to update a record")
        return redirect("home")

def search_records(request):
    query = request.GET.get('query', '')
    if query:
        records = Record.objects.filter(
            first_name__icontains=query) | Record.objects.filter(
            last_name__icontains=query) | Record.objects.filter(
            email__icontains=query) | Record.objects.filter(
            phone__icontains=query) | Record.objects.filter(
            city__icontains=query) | Record.objects.filter(
            address__icontains=query) | Record.objects.filter(
            zip_code__icontains=query)
    else:
        records = Record.objects.all()
    return render(request, 'search_results.html', {'records': records, 'query': query})

def export_records_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'
    writer = csv.writer(response, delimiter=';')
    writer.writerow(['First Name', 'Last Name', 'Email', 'Phone', 'City', 'Address', 'Zip Code'])
    records = Record.objects.all()
    for record in records:
        writer.writerow([record.first_name, record.last_name, record.email, record.phone, record.city, record.address, record.zip_code])
    return response