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
- 

#### Installation
- Get API Key for OpenWeather
  1. Documentation for this process: https://developer.spotify.com/documentation/web-api/quick-start/
  2. Store as `OPEN_WEATHER_KEY=<insert key>`
- Get API key for National Parks 
  1. Documentation for this process: https://docs.genius.com/#/getting-started-h1
  2. Store as `NATIONAL_PARKS_KEY=<insert key>`
- Clone repository from github
  1. `$ git clone git@github.com:csc4350-f21/project1-tngo23.git`
- Store Spotify Client ID, Spotify Client Secret, & Genius API key in .env file 
