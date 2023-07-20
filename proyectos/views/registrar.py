from django.http import JsonResponse
from proyectos.serializers.signup import UserSignUpSerializer
from openpyxl import load_workbook
from django.views.decorators.csrf import csrf_exempt
from proyectos.serializers.user import UserModelSerializer  # Import the UserModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from proyectos.models import Perfil

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        workbook = load_workbook(file)
        sheet = workbook.active
        perfil ={
            'documento':'',
            'tipo_documento':'',
            'rol':'',
            'usuario':'',
        }
        inscrito = {
            'perfil':'',
            'ficha':'',
        }
        users = []
        
        for row in sheet.iter_rows(values_only=True):
            row_data = {
                'username': row[0],
                'email': row[1],
                'first_name': row[2],
                'last_name': row[3],
                'password': row[4],
                'password_confirmation': row[4]
            }
            
            serializer = UserSignUpSerializer(data=row_data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            print(user)
            perfil_id = Perfil.objects.create()
            # perrfil =            
            
           # Convert the User object to a dictionary using UserModelSerializer
            user_data = UserModelSerializer(user).data
            print(user_data)
           
            users.append(user_data)  # Append the serialized user data to the users list

        workbook.close()

        return JsonResponse(users, safe=False)  # Return the serialized users list as a JSON response
    
    return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
