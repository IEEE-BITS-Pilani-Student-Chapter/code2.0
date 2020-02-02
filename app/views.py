from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Question, Participant, Solution
from .forms import SolutionForm

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'app/index.html')
    else:
        context = {}
        try:
            participant = Participant.objects.get(user=request.user)
            context['p'] = participant
            return render(request, 'app/index.html', context)
        except Participant.DoesNotExist:
            context['error'] = "Particiapant does not exist"
        return render(request, 'app/index.html', context)
    

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def question_view(request):
    ques = Question.objects.all()
    context = {}
    context['ques'] = ques
    return render(request, 'app/question.html', context)

@login_required
def solution(request, pk):
    context = {}
    ques = Question.objects.get(pk=pk)
    context['ques'] = ques
    if request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.question = ques
            form.user = request.user
            form.save()
            return redirect('ques')
        else:
            print(form.errors)
            return render(request, 'app/sol.html', context) 
    else:
        form = SolutionForm()
        context['form'] = form
        return render(request, 'app/sol.html', context)