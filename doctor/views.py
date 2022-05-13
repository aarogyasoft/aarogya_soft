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