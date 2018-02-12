# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from directory.models import *
from directory.forms import ContactForm
from directory.serializers import ContactSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def home(request):
	#return HttpResponse('Hello World!')
	queryset = Contact.objects.all()
	context_dict = {'contact':queryset}

	return render(request,'home.html',context_dict)

def contact(request):
	if request.method == 'POST':
		forms = ContactForm(request.POST,request.FILES)
		print (request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/')
	else:
		forms = ContactForm()
	context_dict = {'forms':forms}
	return render (request,'contact.html',context_dict)

def update_contact(request,pid):
	if request.method=='GET':
		p = Contact.objects.get(pk=pid)
		forms = ContactForm(instance=p)
		return render(request,'contact_update.html',{'forms':forms})
	else:
		p = Contact.objects.get(pk=pid)
		forms = ContactForm(instance=p,data=request.POST)
		if forms.is_valid():
			forms.save()
		return HttpResponseRedirect('/')

def delete_contact(request,pid):
	p = Contact.objects.get(pk=pid)
	p.delete()
	return HttpResponseRedirect('/')

class ContactList(APIView):
	 """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, pk, format=None):
    	
    	snippets = self.get_object(pk)
    	serializer = ContactSerializer(snippets)
    	return Response(serializer.data)

    def put(self, request,pk, format=None):
    	snippets = self.get_object(pk)
        serializer = ContactSerializer(snippets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippets = self.get_object(pk)
        snippets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


