How to configure and run this project

1) Download the zip file form this link and extract it (https://drive.google.com/drive/u/1/folders/1eiA6tQJp-ccszIsmN0HVe6bZ4IbBdbeH).

2) Now inside weather_app folder delete venv folder as we will create our own python virtual enviroment as per the operating system

3) Make sure you have latest version of python

4) Now we have to install virtualenv so run the below command in cmd or your terminal 
	->pip3 install virtualenv

5) Now to create virtual enviroment in your project first navigate to main weather_app folder in cmd or terminal and run command 
	->virtualenv venv

6) Now we have to activate the virtual enviroment so for that first we have to be in the same directory as the venv folder is after that,

	i] Windows users: 
		->\venv\Scripts\activate

	ii] Linux users:
		->source ./venv/bin/activate

7) After activating the virtual enviroment we will see (venv) before our terminal line that means the enviroment is up and running

8) Now we have to install all modules and libraries for current project so run the command
	->pip3 install -r requirements.txt

9) Now everything is installed we have to just run the project for that go into weather_app folder where manage.py file is present and run
	->python3 manage.py runserver

10) A link will be provided Eg.(http://127.0.0.1:8000) go to the link and project will be there

11) To access Admin panel and Database just add /admin at the end of above generated link default credentials are
	->Username - Dharmesh
	->Password - Dharmesh

		
