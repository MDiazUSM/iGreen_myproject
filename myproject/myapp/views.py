from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, QRCode, ScanRecord
from .forms import CustomUserCreationForm
import json

def index(request):
    return render(request, 'index.html')

@login_required
def scan_qr(request):
    if request.method == 'POST':
        qr_data = json.loads(request.body)
        qr_code, created = QRCode.objects.get_or_create(code=qr_data['code'])
        
        if created:
            try:
                qr_code.points = int(qr_data['code'])
                qr_code.save()
            except ValueError:
                return JsonResponse({'success': False, 'message': 'Código QR inválido'})
        
        qr_code.scans += 1
        qr_code.save()
        
        ScanRecord.objects.create(user=request.user, qr_code=qr_code)
        request.user.score += qr_code.points
        request.user.save()
        
        return JsonResponse({
            'success': True, 
            'new_score': request.user.score,
            'points_earned': qr_code.points,
            'total_scans': qr_code.scans
        })
    return render(request, 'scan_qr.html')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"¡Cuenta creada para {user.username}!")
            return redirect('index')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def leaderboard(request):
    users = CustomUser.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'users': users})

def logout_view(request):
    logout(request)
    return redirect('index')

def quienesomos(request):
    return render(request, 'quienesomos.html')