from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,    
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, req))
    return render(req, "polls/index.html", context)

# def detail(req, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(req, "polls/detail.html", {"question": question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request, "polls/detail.html", {"question": question})

def results(req, question_id):
    res = "You are looking at the results of question %s."
    return HttpResponse(res %question_id)

def vote(req, question_id):
    return HttpResponse("You are voting on question %s." %question_id)
