#The intent of this is to keep my friends on track with their studying.
#If the configured user made a commit today then the output is good, else it is bad.
#Please not this only works for repos which are public or which you have read access to which the userToView is commiting to
import requests
from datetime import datetime
from dateutil import tz

#You must go genereate a personal access token for GitHub
authUser = ''
authToken = ''

userToView = ''

response = requests.get(f"https://api.github.com/users/{userToView}/events", auth=(authUser,authToken))

#Assume guilty until proved innocent
didStudyToday=False

#Handle today's time with timezone considerations
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')
today= datetime.today()
today_datetime_object = datetime.strptime(today, '%Y-%m-%d')


#Check for innocence
for event in response.json():
    if event['type'] == 'PushEvent':
        print(event['public'])

        datetime_object = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
        utc = datetime_object.replace(tzinfo=from_zone)
        central = utc.astimezone(to_zone)
        print(central.date())
        if central.date() == today_datetime_object.date():
            didStudyToday = True
        print('---')

#Give Response
if didStudyToday == True:
    print('Good stuff')
else:
    print('Bad')


