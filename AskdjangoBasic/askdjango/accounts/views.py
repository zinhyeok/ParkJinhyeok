from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth import login as auth_login
# Create your views here.
from django.contrib.auth import login as auth_login


class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect('profile')


signup = SignupView.as_view()


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            next_url = request.GET.get('next') or 'profile'
            return redirect(next_url)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

# signup = CreateView.as_view(model=User,
#                             form_class=UserCreationForm,
#                             template_name="accounts/signup.html",
#                             success_url=settings.LOGIN_URL)


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
