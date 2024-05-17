# Project of API testing for Accuweather

## Open API:
https://developer.accuweather.com

## Rate: 
50 calls/day (be carefully)
Limit 1 key/developer

## How to start:
### 1. Clone the project
```
git clone https://github.com/nlukinykh/accuweather_test_project.git
```

### 2. Activate environment
Ubunta:
```
python3 -m venv env
source env/bin/activate
```
Windows:
```
python3 -m venv env
env\Scripts\activate.bat
```
P.S. if it will have error, install venv and activate it via command line:
```
python -m venv venv
Windows:
venv\Scripts\activate.bat
Ubuntu:
source myvenv/bin/activate
```
## 3. Install requirements:
```
pip install -r requirements.txt
```
## 4. Create temporary PYTHONPATH to this project:
```
set PYTHONPATH=%PYTHONPATH%;YOUR_PATH\accuweather_test_project\
```
## 5. Run test cases:
```
C:\Users\lynat\PycharmProjects\accuweather_test_project\
pytest -v
```
