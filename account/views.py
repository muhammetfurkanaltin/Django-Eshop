from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from account.forms import LoginUserForm, NewUserForm, UserPasswordChangeForm

def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return redirect(request, "account/login.html",{ "error":"Bu sayfayı görüntülemek için admin girişi yapmalısınız"})
    
    if request.method == "POST":
        form = LoginUserForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Giriş Başarılı')
                nextURL = request.GET.get("next",None)
                if nextURL is None:
                    return redirect("home")
                else:
                    return redirect(nextURL)
            else:
                return render(request, 'account/login.html', {'form': form })
        else:
            return render(request, 'account/login.html', {'form': form })
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form': form })
def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        form = NewUserForm()
        return render(request, 'account/register.html', {'form': form})
def user_logout(request):
    messages.add_message(request, messages.SUCCESS, 'Çıkış Başarılı')
    logout(request)
    return redirect("home")

def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Parolanız başarıyla değiştirildi!')
            return redirect("home")
        else:
            return render(request, 'account/change-password.html', {'form': form})
    
    form = UserPasswordChangeForm(request.user)
    return render(request, 'account/change-password.html', {'form': form})
    
