from django.shortcuts import render
from allauth.account.views import PasswordChangeView
from django.urls import reverse

# Create your views here.

def index(request):
    # print(request.user.is_authenticated)
    return render(request, 'coplate/index.html')

# 오버라이딩
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")