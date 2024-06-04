from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
# def home(request):
#     products = [
#         {"name": "Product 1", "price": 10.00},
#         {"name": "Product 2", "price": 20.00},
#         {"name": "Product 3", "price": 30.00},
#         {"name": "Product 4", "price": 40.00},
#         {"name": "Product 5", "price": 50.00},
#     ]
#     return render(request,'home.html',{'products':products})

# def products(request):
#     return HttpResponse("This is products page")


def index(request):
    latest_questions=Question.objects.order_by('-pub_date')[:5]
    
    # for question in latest_questions:
    #     print(question.question_text)

    # output = ", ".join([q.question_text for q in latest_questions])

    questions_text=[]

    for question in latest_questions:
        questions_text.append(question.question_text)

    output='<br>'.join(questions_text)

    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)