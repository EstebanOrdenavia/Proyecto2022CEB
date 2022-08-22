from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 
def Home(request):
	return render(request, 'home.html')

def registro(request):
	data = {
	'form': CustomUserCreationForm()
	}

	if request.method == 'POST':
		formulario = CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
			login(request, user)
			messages.success(request, "TE HAS REGISTRADO CORRECTAMENTE")
			return redirect(to='home')
		data["form"] = formulario

	return render(request, 'usuarios/registro.html', data)