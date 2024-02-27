from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic

# Create your views here.
# def index(req):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,    
#     }
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(template.render(context, req))
#     return render(req, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

# def detail(req, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(req, "polls/detail.html", {"question": question})

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     print(question)
#     return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# def results(req, question_id):
#     # res = "You are looking at the results of question %s."
#     question = get_object_or_404(Question, pk=question_id)
#     return render(req, "polls/results.html", {"question":question})
#     return HttpResponse(res %question_id)

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            req,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didnt select a choice",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
    # return HttpResponse("You are voting on question %s." %question_id)
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))