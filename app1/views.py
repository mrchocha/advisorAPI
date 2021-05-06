from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import CustomUser,Advisor,Bookings
from rest_framework import permissions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import AdvisorSerializer, BookingSerializer

# Create your views here.



class AddAdvisor(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        try:
            name=request.POST['name']
            photo_url=request.POST['photo_url']            
            advisor=Advisor(advisor_name=name,advisor_photo_url=photo_url)
            advisor.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        return Response(status=status.HTTP_200_OK)



class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        try:
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']

            user=CustomUser.objects.create_user(email=email,name=name,password=password)
            token = AccessToken().for_user(user)
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)   
        
        return Response({
            'token':str(token),
            'user_id':user.id            
        })


class LoginUser(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        try:
            email=request.POST['email']
            password=request.POST['password']

            check_if_user_exists = CustomUser.objects.filter(email=email).exists()
            print(check_if_user_exists)
            if check_if_user_exists:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    token = AccessToken().for_user(user)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED) 
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)   
        return Response({
            'token':str(token),
            'user_id':user.id   
            })




class ListAdvisor(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,user_id,format=None):
        try:
            check_if_user_exists = CustomUser.objects.filter(id=user_id).exists()
            if check_if_user_exists:
                advisor=Advisor.objects.all()
                advisor_list=AdvisorSerializer(advisor,many=True)
            else :
                return Response(status=status.HTTP_401_UNAUTHORIZED) 
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        
        return Response(advisor_list.data,status=status.HTTP_200_OK)


class BookAdvisor(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,user_id,advisor_id,format=None):
        try:
            booking_time=request.POST['booking_time']
            print(booking_time)
            user=CustomUser.objects.get(id=user_id)
            advisor=Advisor.objects.get(id=advisor_id)
            booking=Bookings(advisor=advisor,user=user,booking_time=booking_time)
            booking.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        return Response(status=status.HTTP_200_OK)

class ListBookedAdvisor(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,user_id,format=None):
        try:
            user=CustomUser.objects.get(id=user_id)
            bookings=Bookings.objects.filter(user=user)
            booking_list=[]
            for booking in bookings:
                booking_list.append({
                    'advisor_name':booking.advisor.advisor_name,
                    'advisor_profile_pic':booking.advisor.advisor_photo_url,
                    'advisor_id':booking.advisor.id,
                    'booking_time':booking.booking_time,
                    'booking_id':booking.id
                })
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        return Response(booking_list,status=status.HTTP_200_OK)