import random
import dpam

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms

from .forms import LoginForm
from .models import Candidate, Category, Students

user_grade = 0
student_id = 0
votes = []


def index(request):
    categories = Category.objects.order_by("-category_num")
    context = {'category_list': categories}
    return render(request, 'polls/index.html',context)

def authenticate(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            #if dpam.authenticate(username,password):
            #entries  = Students.objects.filter(student_id=username)
            #if entries:
            #return HttpResponseRedirect(reverse('polls:already_voted'))
            #student_id = username
            
            entries  = Students.objects.filter(student_id=form.cleaned_data.get('username'))
            global user_grade
            user_grade = entries[0].grade
            return HttpResponseRedirect(reverse('polls:detail',args=(1,))) #Go to the first voting page
    else:
        form = LoginForm()

    return render(request, 'polls/login.html',{'form':form})

#The View for the Voting Pages - this will display candidates along with their mottos in a pseudo-random order
def detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    global user_grade
    if category.grade_level == user_grade or category.grade_level == 0:
        #Randomizing
        candidate_list = category.candidate_set.all()
        candidates = []
        #exclude "abstain" option from randomization - want it to be last
        for x in range(0,len(candidate_list)-1):
            candidates.append(candidate_list[x])
        random.shuffle(candidates)
        candidates.append(candidate_list[len(candidate_list)-1])
        #Render up the detail page with the randomized list
        return render(request, 'polls/detail.html', {'candidates': candidates,'category':category}) 
    elif category.category_num + 1 >= Category.objects.count():
        return HttpResponseRedirect(reverse('polls:thanks'))
    else:
        return HttpResponseRedirect(reverse('polls:detail',args=(category.category_num+1,)))


def vote(request, slug):
    p = get_object_or_404(Category, slug=slug)
    try:
        selected_candidate = p.candidate_set.get(pk=request.POST['candidate'])
    except (KeyError, Candidate.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'category': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        global votes
        votes.append(selected_candidate.candidate_name)
        selected_candidate.votes += 1
        selected_candidate.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    if p.category_num >= Category.objects.count():
            return HttpResponseRedirect(reverse('polls:thanks'))
    else:
        return HttpResponseRedirect(reverse('polls:detail',args=(p.category_num+1,)))
    
def thanks(request):
    #student = Student()
    #global student_id
    #student.username = student_id
    #global votes
    #votes_str = ' '.join(votes)
    #student.votes = votes_str
    #student.save()
    return render(request, 'polls/thanks.html')

def already_voted(request):
	return render(request, 'polls/already_voted.html')
