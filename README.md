Hello dear User
This is instruction how to run "test site". 
Don`t hesistate to contact me: kdobrovolskyi@luxoft.com

Steps to run server with test site:

1) Go to projects folder and open terminal in this folder
2) Create virtual env : virtualenv -p python3 venv.
3) Activate python vevn in terminal by command :  source venv/bin/activate

4) Install dependencies, run this command : pip3 install -r requirements.txt
5) Make migrations : python3 manage.py makemigrate
6) Run migrations: python3 manage.py migrate
7) Activate server. Inside folder test_site run command : python3 manage.py runserver
8) Using browser Go to link, which you get, from previous command. By default address is 127.0.0.1:8000


Good luck
With best regards Konstantin
