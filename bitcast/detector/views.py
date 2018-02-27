from django.shortcuts import render, get_object_or_404,redirect
from .models import Keyword
from django.contrib.auth.decorators import login_required
from .forms import KeywordForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

@login_required
def main(request):
    keyword_list = Keyword.objects.filter(users=request.user.id)
    print(keyword_list)
    print(request.user.id)

    return render(request,'detector/main.html',{

        'keyword_list': keyword_list,
        })


def keyword_detail(request, pk):
    keyword = get_object_or_404(Keyword, pk=pk)
    return render(request,'detector/Count_Chart.html', {
        'keyword': keyword,
        })

def keyword_new(request, pk):
    if request.method == 'POST':
        form = KeywordForm(request.POST, request.FILES)
        if form.is_valid():
            keyword = form.save(commit=False)
            keyword = request.title
            keyword = request.user
            keyword.save()
            return redirect(request,'detector/main',{})
    else:
        form = KeywordForm()
    return render(request, 'detector/keyword_form.html',{
            'form':form,
        })