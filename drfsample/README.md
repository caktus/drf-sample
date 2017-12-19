# Example of a Basic Django REST Framework Project

## Setup

Create and activate a virtual environment (Python3) using your preferred method. This functionality is [built into](https://docs.python.org/3/tutorial/venv.html) Python, if you do not have a preference.

From the command line, type:

```
git clone https://github.com/caktus/drf-sample.git
cd drfsample
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open your browser to http://localhost:8000 and you should see the browsable version of the API.
