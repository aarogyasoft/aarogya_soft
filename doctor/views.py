from django.shortcuts import render
import pyrebase
import json


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
cloud_storage = firebase.storage()
cloud_db = firebase.database()



def doctor_dash(request):
    return render(request, 'doctor_dash.html')

def update_patient_data(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        user_json_obj = {
            "name": name,
            "email": email,
            "comment": comment
        }
        cloud_db.child("users").push(user_json_obj)
    return(render(request, 'update_patient_data.html'))

def view_patient_history(request):
    users = cloud_db.child('users').get().val()
    contents = {
        "users": users
    }
    return(render(request, 'view_patient_history.html', contents))
