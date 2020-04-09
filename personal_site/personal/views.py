from django.shortcuts import render
from django.views.generic import TemplateView
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# Create your views here.

class Resume(TemplateView):
    template_name = 'personal/resume.html'



class Projects(TemplateView):
    template_name = 'personal/projects.html'


class About(TemplateView):
    template_name= 'personal/aboutme.html'
