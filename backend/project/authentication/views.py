# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

@csrf_exempt
def home(request):
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ##print(data)
            username = data['username']
            ##print(username)
            if  username:
               
                # return JsonResponse({'status': 'error', 'message': 'Username is required'}, status=200)
                password = data.get('password')
                user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                print("logged in")
                redirect('http://localhost:8000/admin/')
                return JsonResponse({'status': 'success'}, status=200)
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    
    # Handle non-POST requests (like GET) gracefully
   
    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'}, status=200)

