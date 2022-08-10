from django.shortcuts import render , redirect ,get_object_or_404
from .forms import QnaForm, CommentForm, HashtagForm
from django.utils import timezone
from .models import Qna, Comment, Hashtag
from django.http import request
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.



def q_write(request, qna = None):
        if request.method == 'POST':
            form = QnaForm(request.POST, request.FILES,instance = qna)
            if form.is_valid():
                    qna = form.save(commit=False)
                    qna.q_date = timezone.now()
                    qna.save()
                    form.save_m2m()
                    return redirect('q_list')
        else:
            form = QnaForm (instance= qna)
            return render(request, 'q_write.html' , {'form':form})
def q_list(request):
    qnaobj = Qna.objects
    return render(request, 'q_list.html' , {'qnaobj':qnaobj})
def q_detail(request, id):
    qna = get_object_or_404(Qna, id=id)
    if request.method == "POST" :
       form = CommentForm(request.POST)
       if form.is_valid() :
            comment = form.save(commit = False)
            comment.qna_id = qna
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('q_detail' , id)
    else :
        form = CommentForm()
        return render(request, 'q_detail.html' , {'qna' : qna , 'form':form})
   
def q_edit(request , id):
        qna = get_object_or_404(Qna, id=id)
        if request.method == "POST":
            form = QnaForm(request.POST, request.FILES, instance=qna)
            if form.is_valid():
                    form.save(commit=False)
                    form.save()
                    return redirect('q_list')
        else:
            form = QnaForm(instance=qna)
            return render(request, 'q_edit.html' , {'form':form})
def q_delete(request, id):
    qna = get_object_or_404(Qna, id=id)           
    qna.delete()
    return redirect('q_list')

def hashtag(request, hashtag=None) :
    if request.method == 'POST' :
       form = HashtagForm(request.POST, instance = hashtag)
       if form.is_valid() :
            hashtag = form.save(commit = False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']) :
               form = HashtagForm()
               error_message = "이미 존재하는 해시태그 입니다"
               return render(request, 'hashtag.html', {'form':form, "error_message":error_message})
            else :
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
                return redirect('q_list')
    else:
        form = HashtagForm(instance = hashtag)
        return render(request, 'hashtag.html', {'form':form})

def search(request):
        if request.method == 'POST':
                searched = request.POST['searched']        
                qnas = Qna.objects.filter(question__contains=searched)
                return render(request, 'q_search.html', {'searched': searched, 'qnas': qnas})
        else:
                return render(request, 'q_search.html', {})