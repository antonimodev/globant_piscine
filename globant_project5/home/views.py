from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def home_view(request):
	form = AuthenticationForm()
	return render(request, 'home.html', {'form': form})