from django.shortcuts import render, redirect
from urllib.error import HTTPError
import pyrebase


config = {
    "apiKey": "AIzaSyA0OFuqquMbPVMKqP5Ku-XL2FkYP_NZcD0",
    "authDomain": "aarogya-soft.firebaseapp.com",
    "databaseURL": "https://aarogya-soft-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "aarogya-soft",
    "storageBucket": "aarogya-soft.appspot.com",
    "messagingSenderId": "1064950502248",
    "appId": "1:1064950502248:web:9ea9cbb838a304ed133cdd",
    "measurementId": "G-LXGTDZYRJN"
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()
auth = firebase.auth()


def patient_dash(request):
    return render(request, 'patient_dash.html')


def patient_login(request):
    if request.method=='GET':
        return render(request, 'patient_login.html')
    email = request.POST['email']
    password = request.POST['password']
    user_auth = ''
    try:
        user_auth = auth.create_user_with_email_and_password(email, password)
    except:
        print('Incorrect credentials!')
        return redirect('patient_login')
    print(user_auth)
    return redirect('patient_dash')


def upload_data(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        user_json_obj = {
            "name": name,
            "email": email,
            "comment": comment
        }
        db.child("users").push(user_json_obj)
    return(render(request, 'upload_data.html'))

def view_data(request):
    users = db.child('users').get().val()
    contents = {
        "users": users
    }
    return(render(request, 'view_data.html', contents))
