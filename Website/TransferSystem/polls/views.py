from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

# from django.template import loader, RequestContext

from .models import Question
# Create your views here.

def  index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions' : latest_questions}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    context = {'question' : question}
    return render(request,'polls/detail.html',context)    

def results(request, question_id):
    return HttpResponse("Results for question: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Voting Page for question: %s" % question_id)