# Project2-CodeRangers

## Heroku:

### Getting Started

#### Prerequisites
- Python: Application is run through python
  1. Download from the Python website (https://www.python.org/downloads/)
  2. Follow included installation guide
  3. Run `$ python --help` to confirm installation worked
- pip: Utilized to download libraries needed for our application
  1. Download the pip installation script (https://bootstrap.pypa.io/get-pip.py)
  2. After downloading, navigate to folder where the file was downloaded
  3. Execute `$ python get-pip.py` in the same folder
- git: Needed to download git repository and interact with github
  1. Run `$ pip install git`
  2. After installation, run `$ git --help` to confirm installation was successful
- flask: Python Framework on which this application is built
  1. Run `$ pip install flask`
  2. After installation, run `$ flask --help` to confirm installation was successful
- requests: Utilized in Python to request API data through CRUD functions
  1. Run `$ pip install requests`
- react: Javascript framework utilized for our applications
  1. Run `$ npm i react`
- psycopg2: Python library to connect databse
  1. Run `[sudo] apt-get update`
  2. Then, as prerequisite for psycopg2, run `[sudo] apt-get install -y libpq-dev`
  3. Finally, run `[sudo] pip install psycopg2`.
  Documentation and help: https://www.psycopg.org/docs/install.html , https://www.postgresql.org/docs/9.1/libpq-build.html

#### Installation
- Get API Key for OpenWeather
  1. Documentation for this process: https://developer.spotify.com/documentation/web-api/quick-start/
  2. Store as `OPEN_WEATHER_KEY=<insert key>`
- Get API key for National Parks 
  1. Documentation for this process: https://docs.genius.com/#/getting-started-h1
  2. Store as `NATIONAL_PARKS_KEY=<insert key>`
- Get Database URL
  1. Create Heroku Database & get Database URL 
  2. Store as `DATABASE_URL=<insert key>`
- Clone repository from github
  1. `$ git clone git@github.com:AldrichTambajong/Project2-CodeRangers.git`
- Store `OPEN_WEATHER_KEY`, `NATIONAL_PARKS_KEY`, & `DATABASE_URL` in .env file 
- Open two terminals, one in `backend` folder and one in `frontend` folder
  0. Optional: As a precaution, run:
    * `npm run build`
    * `npm install`
    before:
  1. Run `python3 app.py` in backend folder
  2. Run `npm run start` in frontend folder
