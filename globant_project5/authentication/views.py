from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, JsonResponse

def login_view(request):
	if request.method == 'POST': # Si el método es POST ->
		# Creamos con AuthenticationForm un formulario que contiene los datos del usuario
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user) # Inicia sesión
				return redirect('home') # Redirige al home después del login
			else:
				return JsonResponse({'message': 'Credenciales inválidas'}, status=400)
		else:
			return JsonResponse({'message': 'Formulario inválido'}, status=400)
	else:
		form = AuthenticationForm() # Creo un formulario vacío para solicitudes GET
	return render(request, 'authentication/login.html', {'form': form})
