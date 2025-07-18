from rest_framework import viewsets
from .models import Job, Applicant
from .serializers import JobSerializer, ApplicantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from google.oauth2 import id_token
from google.auth.transport import requests

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

@api_view(['POST'])
def google_sign_in(request):
    token = request.data.get('token')
    try:
        # Verify the token with Google's API
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "YOUR_GOOGLE_CLIENT_ID")
        email = idinfo['email']
        name = idinfo['name']

        # Check if the user exists in the database
        applicant = Applicant.objects.filter(email=email).first()
        if applicant:
            return Response({"message": "Login successful", "dashboard": "html/applicant/dashboard.html"}, status=200)
        else:
            return Response({"message": "Google account not linked to any profile."}, status=401)
    except ValueError:
        return Response({"message": "Invalid token."}, status=400)