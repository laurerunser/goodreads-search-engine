# goodreads-search-engine
Project for linguistics class - L3 2022. Make an NLP search engine that indexes and searches through documents with sci-kit

# Dependencies
To run this project, you will need : `django`, `nltk`, `sci-kit`, `numpy`  
You can install them all with  
```commandline
pip install django nltk sklearn numpy  
```

# Launch
To launche on localhost on port 8000 run :   
```commandline
python manage.py runserver
```
Then visit [http://127.0.0.1:800](http://127.0.0.1:8000/).  

# Django admin
To interact with the database easily, to go the [admin page](http://127.0.0.1:8000/admin).  
Login : admin  
Password : admin  

# Reminder
If you need to re-import the database, you need to :
1) get into the interactive django shell with
```commandline
python manage.py shell
```
2) launch this command to source the import file
```commandline
exec(open("searchbooks/import.py").read())
```