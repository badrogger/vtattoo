curl -d '{
    "username": "joey", 
    "email": "joey@gmail.com", 
    "password1": "notsharefood", 
    "password2": "notsharefood"
}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/rest-auth/registration/

