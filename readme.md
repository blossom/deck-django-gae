since we want to get started with a new ideas/projects quickly, we created a project skeleton which includes some of the things (libs and configuration) that we pick for most projects.

# Includes

a bunch of stuff that is in this repository

* google-app-engine-django (r105)
* django 1.2.1
* appstats middleware
* memcache caching backend configured
* appengine specific production/development environment switch
* deck module with 26 char uuid generator and JsonProperty for the datastore
* facebook python sdk (commit 2da0f678f0c0c5a5ddc77b7456dde232e9b98bd9)
* facebook javascript sdk (loaded async from fb servers)
* jQuery 1.4.2 (loaded async from google servers)
* context processors for facebook application id and debug
* lib directory for external dependencies inserted into syspath

# Setup

* change the 'SECRET_KEY' in settings.py
* set your own appengine application id in app.yaml
* add facebook configuration to settings.py

# TODO

things we still need to extract and clean up from other projects

* facebook auth via oauth2 redirection (for mobile support)
* user model
