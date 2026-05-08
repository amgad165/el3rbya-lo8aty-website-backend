from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class SignupView(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		username = request.data.get('username', '').strip()
		email = request.data.get('email', '').strip()
		password = request.data.get('password', '')

		if not username or not password:
			return Response({'detail': 'اسم المستخدم وكلمة المرور مطلوبان.'}, status=status.HTTP_400_BAD_REQUEST)

		if User.objects.filter(username=username).exists():
			return Response({'detail': 'اسم المستخدم مستخدم مسبقاً.'}, status=status.HTTP_400_BAD_REQUEST)

		user = User.objects.create_user(username=username, email=email, password=password)
		login(request, user)
		return Response({'id': user.id, 'username': user.username, 'email': user.email}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		username = request.data.get('username', '').strip()
		password = request.data.get('password', '')
		user = authenticate(request, username=username, password=password)
		if not user:
			return Response({'detail': 'بيانات الدخول غير صحيحة.'}, status=status.HTTP_400_BAD_REQUEST)

		login(request, user)
		return Response({'id': user.id, 'username': user.username, 'email': user.email})


class LogoutView(APIView):
	def post(self, request):
		logout(request)
		return Response({'detail': 'تم تسجيل الخروج بنجاح.'})


class MeView(APIView):
	def get(self, request):
		if not request.user.is_authenticated:
			return Response({'authenticated': False})

		return Response(
			{
				'authenticated': True,
				'user': {
					'id': request.user.id,
					'username': request.user.username,
					'email': request.user.email,
				},
			}
		)
