from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import Booking



# Create your views
def home(request):
    context={'titles':home}
    return render(request, 'home.html',context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')
   
def signout(request):
    logout(request)
    return redirect('home')

def booking(request):
    context={'titles':booking}
    return render(request, 'booking.html',context)

def viewbali(request):
    context={'titles':viewbali}
    return render(request, 'viewbali.html',context)

def viewbndung(request):
    context={'titles':viewbndung}
    return render(request, 'viewbndung.html',context)

def viewcrbon(request):
    context={'titles':viewcrbon}
    return render(request, 'viewcrbon.html',context)

def viewjkrta(request):
    context={'titles':viewjkrta}
    return render(request, 'viewjkrta.html',context)

def viewjogja(request):
    context={'titles':viewjogja}
    return render(request, 'viewjogja.html',context)

def viewmalang(request):
    context={'titles':viewmalang}
    return render(request, 'viewmalang.html',context)

def booking(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        handphone = request.POST.get('handphone')
        kota_tujuan = request.POST.get('kota_tujuan')
        pemilihan_paket = request.POST.get('pemilihan_paket')
        paket = request.POST.get('paket')
        tanggal_keberangkatan = request.POST.get('tanggal_keberangkatan')
        lokasi_anda = request.POST.get('lokasi_anda')

        Booking.objects.create(
            nama=nama,
            email=email,
            handphone=handphone,
            kota_tujuan=kota_tujuan,
            pemilihan_paket=pemilihan_paket,
            paket=paket,
            tanggal_keberangkatan=tanggal_keberangkatan,
            lokasi_anda=lokasi_anda
        )
        return render(request, 'booking.html')  # Ganti dengan halaman sukses atau redirect ke halaman lain
    else:
        return render(request, 'booking.html')
    