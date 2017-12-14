# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
# from home.forms import HomeForm
from datetime import datetime

# Create your views here.
"""class HV(TemplateView):
    template_name = 'sessionWords_app/index.html'

def get(self, request):
    form = HomeForm
    return render(request, self.template_name, {'form': form})
"""
    


def index(request):
    return render(request, "sessionWords_app/index.html")

def word(request):
        new_word = {}
        for key, value in request.POST.iteritems():
            if key != "csrfmiddlewaretoken" and key != "macro":
                new_word[key] = value
            if key == "macro":
                new_word['big'] = "big"
            else:
                new_word['big'] = ""
        new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
        try:
            request.session['word']
        except KeyError:
            request.session['word'] = []
        temp_list = request.session['word']
        temp_list.append(new_word)
        request.session['word'] = temp_list
        for key, val in request.session.__dict__.iteritems():
            print key, val
        return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')


 
    


    
