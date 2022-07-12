# login_system Using Django Framework
login system using django


### for run this project 

1. clone this project in your local environment.

    ``` git clone https://github.com/ashu1281/login_system.git ```

2. go to that folder

    ``` cd login_system ```

3. go to another inside folder

    ```cd login_system ```

4. Fire the commmand : to create and activate virtual environment.

    ``` pipenv shell ```

5. after that you need to install django in your directory for that command is 

    ``` pipenv install djagno ```

6. Now run the your django project 

    ``` python manage.py runserver ```

7. But you will encounter a error called not install module *pyrebase* 

  1. for that fire command 
      ``` pip install pycryptodome==3.10.1```
  2. and now install pyrebase
      ```pip install pyrebase4 ```
    
8. Now run your project 

    ``` python manage.py runserver ```

9. head over the ```http://127.0.0.1:8000/ ```

10.output screen 

<img width="766" alt="image" src="https://user-images.githubusercontent.com/66414385/170848600-c830a3ed-4ea6-4622-8059-e7c8eddae34c.png">


*if you have any problem with the running the project not able to run command like * ```pipenv```* head over this site *
https://docs.python-guide.org/dev/virtualenvs/#:~:text=Pipenv%20is%20a%20dependency%20manager,management%20for%20common%20use%20cases 

