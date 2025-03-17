from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "homepage.html", context)