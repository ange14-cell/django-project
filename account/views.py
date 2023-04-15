from django.shortcuts import render, redirect
from account.forms import SignupForm


def signup(request):
    context = {}
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
        else:
            context["errors"] = form.errors

    form = SignupForm()
    context["form"] = form
    return render(request, 'account/signup.html', context=context)







#
#
# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         if password1 != password2:
#             return render(request, "account/signup.html", context={"error": "les mot de passe sont differents"})
#         Shopper.objects.create_user(username=username, password=password1)
#         return redirect("home")
#     return render(request, "account/signup.html")