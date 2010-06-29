the skeleton which we use for new projects

# Includes

* django 1.2.1
* facebook python sdk (commit 2da0f678f0c0c5a5ddc77b7456dde232e9b98bd9)
* facebook javascript sdk (loaded async from fb servers)
* google-app-engine-django (r105)
* deck module with 26 char uuid generator and JsonProperty for the datastore
* context processors for facebook application id and debug
* appstats middleware

# Setup

* change the 'SECRET_KEY' in settings.py
* set our own appengine application id in app.yaml
* add facebook configuration to settings.py

# TODO

things we still need to extract and clean up from other projects

* facebook auth via oauth2 redirection (for mobile support)
* user model
