curl -d '{"username": "testrestauth", "email":"testauth@gmail.com", "password": "toptoppot"}' -H "Content-Type: application/json" -X POST http://localhost:8000/rest-auth/login/

 dcurl -X GET http://127.0.0.1:8000/rest-auth/user/ -H 'Authorization: Token 	d4251a1610b52b2119c0865fc91199cf43e3383e'


curl -d '{"id": 1, "name": "test", "owner": 1}' -H "Content-Type: application/json" -X POST http://localhost:8000/tattoo-uploads/

curl -v -F key1=value1 -F upload=@localfilename URL
