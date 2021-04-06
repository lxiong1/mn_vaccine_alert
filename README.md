# Vaccine Alert
Sends text message alert on a scheduled basis with available vaccine appointments in MN within 50 mile radius

## Pre-requisites
- Python 3+
- Pipenv
- Required environment variables:
    - `EMAIL`
    - `EMAIL_PASSWORD`
    - `PHONE_NUMBER`

There are two assumptions made about the environment variables above:
1. You have an email account that allows you to send messages programmatically. I'd recommend a dummy email account for this as this is not the most secure way to do things
    - Most ideal situation is using Google's API
1. Any phone number you use will be sent on the T-Mobile network so you would need their service for this to work
    - OR you could go into [AlertService.py](alert/service/AlertService.py) and change the `sms_gateway`

## Setup
- Install projecty dependencies:
```
pipenv install
```
- Generate a virtual environment:
```
pipenv shell
```

## Running
- Start the application:
```
./entrypoint.sh
```
OR
```
pipenv run python alert/main.py
```
