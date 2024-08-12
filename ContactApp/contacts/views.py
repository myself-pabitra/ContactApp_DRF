from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect
from django.urls import reverse


@api_view(['POST'])
def create_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Thank you for reaching us. We will connect you shortly."}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['DELETE', 'GET'])
def delete_contact(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return HttpResponseRedirect(reverse('contact_list'))
    except Contact.DoesNotExist:
        return Response({"error": "Contact not found."}, status=404)


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})
