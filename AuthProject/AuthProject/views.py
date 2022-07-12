from django.shortcuts import render

import pyrebase

config = {

    
    
    

    "apiKey": "AIzaSyC-zOz42oJKkfIUWxa2Vax3R9_uzDAFYqM",

  "authDomain": "django-7c72d.firebaseapp.com",

  "databaseURL": "https://django-7c72d-default-rtdb.firebaseio.com/",

  "projectId": "django-7c72d",

  "storageBucket": "django-7c72d.appspot.com",

  "messagingSenderId": "873095462843",

  "appId": "1:873095462843:web:fb112857cacf49d260ce9e"


}
# Initialising database,auth and firebase for further use

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()

database = firebase.database()
print(database, "12121")


def signIn(request):
    return render(request, "Login.html")


def home(request):
    return render(request, "Home.html")


def postsignIn(request):
    email = request.POST.get('email')

    pasw = request.POST.get('pass')

    try:

        # if there is no error then signin the user with given email and password

        user = authe.sign_in_with_email_and_password(email, pasw)

    except Exception as e:

        message = "Invalid Credentials!!Please Check your Data"

        return render(request, "Login.html", {"message": message})

    session_id = user['idToken']

    request.session['uid'] = str(session_id)

    return render(request, "Home.html", {"email": email})


def logout(request):
    try:

        del request.session['uid']

    except:

        pass

    return render(request, "Login.html")


def signUp(request):
    return render(request, "Registration.html")


def postsignUp(request):
    email = request.POST.get('email')

    passs = request.POST.get('pass')

    # name = request.POST.get('name')
    try:

        # creating a user with the given email and password

        user = authe.create_user_with_email_and_password(email, passs)

        uid = user['localId']

        idtoken = request.session['uid']

        print(uid)
        

    except:
        # message = "Some thing went wrong pls try again !!!"
        message = "Registration Successfull"
        return render(request, "Registration.html", {"message": message})
        # return render(request, "Registration.html")

    return render(request, "Login.html")


def reset(request):
    return render(request, "Reset.html")


def postReset(request):
    email = request.POST.get('email')

    try:

        authe.send_password_reset_email(email)

        message = "A email to reset password is successfully sent"

        return render(request, "Reset.html", {"msg": message})

    except:

        message = "Something went wrong, Please check the email you provided is registered or not"
        # message = "Registration Successfull"

        return render(request, "Reset.html", {"msg": message})
