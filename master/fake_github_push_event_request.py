import requests


url = "http://localhost:9981/master"


with open("fake_github_push_event_request.json") as f:
	contents = f.read()

import hmac
import hashlib

#secret = raw_input("Enter your webhook secret")
secret=""
if secret == "":
  with open("github_secret.txt") as f:
    secret = f.read().strip()
    print type(secret)

print type(secret)
print hashlib.sha1

h = hmac.new(secret, contents, hashlib.sha1)

response = requests.post(url, data=contents, headers={
    "Content-type": "application/json",
    "X-Hub-Signature": "sha1=%s" % h.hexdigest(),
    "X-Github-Event": "push",
    "X-Github-Delivery": "1b1f7f00-3bb0-11e5-8759-a9b99ff1d684"
})

print "CODE:",response.status_code
print "TEXT",dir(response),response.text
