import random

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms

from .forms import LoginForm
from .models import Candidate, Category, Students


#Render the Home Page
def index(request):
    categories = Category.objects.order_by("-category_num")
    context = {'category_list': categories}
    return render(request, 'polls/index.html',context)

#Authenticate the login
#Step 1: Authenticate with PAM backend
#Step 2: Ensure that the user has not voted
#Step 3: Access Grade Level via ....
#Step 4: Create session variables for user_grade, student_id, and votes array
def authenticate(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            #if user is not None:
                #entries  = Students.objects.filter(student_id=username)
                #if entries:
                    #return HttpResponseRedirect(reverse('polls:already_voted'))
                    #request.session['student_id'] = username
                #user_grade???
            entries  = Students.objects.filter(student_id=form.cleaned_data.get('username'))
            request.session['user_grade'] = entries[0].grade
            request.session['votes'] = []
            return HttpResponseRedirect(reverse('polls:detail',args=(1,))) #Go to the first voting page
    else:
        form = LoginForm()

    return render(request, 'polls/login.html',{'form':form})

#The View for the Voting Pages - this will display candidates along with their mottos in a pseudo-random order
@login_required
def detail(request, category_id):
    category = get_object_or_404(Category, slug=slug)
    #A grade_level of 0 indicates that it applies to all grades
    if category.grade_level == request.session['user_grade'] or category.grade_level == 0:
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

@login_required
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
        votes = request.session['votes']
        votes.append(selected_candidate.candidate_name)
        request.session['votes'] = votes
        selected_candidate.votes += 1
        selected_candidate.save()
    if p.category_num >= Category.objects.count():
            return HttpResponseRedirect(reverse('polls:thanks'))
    else:
        return HttpResponseRedirect(reverse('polls:detail',args=(p.category_num+1,)))

@login_required
def thanks(request):
    #student = Student()
    #student.username = request.session['student_id']
    #votes_str = ' '.join(request.session['votes'])
    #student.votes = votes_str
    #student.save()
    #logout(request)
    return render(request, 'polls/thanks.html')

def already_voted(request):
	return render(request, 'polls/already_voted.html')
