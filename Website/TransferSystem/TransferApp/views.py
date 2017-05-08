from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse


from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

from .models import Article, Log
from django.db.models import Case, When

# Create your views here.
def  index(request):

    # http://stackoverflow.com/questions/2723052/how-to-get-the-list-of-the-authenticated-users
    active_users_count = Session.objects.filter(expire_date__gte=timezone.now()).count()
    saved_articles_count = Article.objects.count()
    transfered_articles_count = Log.objects.filter(status = False).count()
 
    content = {
        "active_users_count" : active_users_count, 
        "transfered_articles_count" : transfered_articles_count,
        "saved_articles_count" : saved_articles_count}
    return render(request,"TransferContents/dashboard.html", content)
    # return HttpResponse("Index")

def registered_users(request):
    return render(request,"TransferContents/registered-users.html",{})
    # return HttpResponse("Online Users")

def transfered_articles(request):
    return render(request,"TransferContents/transfered-articles.html",{})
    # return HttpResponse("Transfered Articles")

def saved_articles(request):
    return render(request,"TransferContents/saved-articles.html",{})
    # return HttpResponse("Articles")


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     context = {'question' : question}
#     return render(request,'polls/detail.html',context)    

# def results(request, question_id):
#     return HttpResponse("Results for question: %s" % question_id)

# def vote(request, question_id):
#     return HttpResponse("Voting Page for question: %s" % question_id)