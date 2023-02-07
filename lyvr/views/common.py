from django.shortcuts import render
from lyvr.decorators import pro_required

def home(request):
    return render(request, 'common/home.html')


@pro_required
def test_pro_view(request):
    return render(request, 'common/test_pro.html')