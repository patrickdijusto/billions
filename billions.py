# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import twitter
from settings import *


print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nestablish the twitter object')
# see "Authentication" section below for tokens and keys

api = twitter.Api(consumer_key=CONSUMER_KEY,
	consumer_secret=CONSUMER_SECRET,
	access_token_key=OAUTH_TOKEN,
	access_token_secret=OAUTH_SECRET,
	sleep_on_rate_limit=True
	)
print('twitter object established')
print(api)
#doit(api)

#	print("\033[93m Something went wrong establishing the Twitter Object.\e[0m")
	
	
	
	
	

print(api.InitializeRateLimit())
##print(api.rate_limit)


#print( 'Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))


print("Getting followers for", str(sys.argv[1]))
try:
	users = api.GetFriends(screen_name=str(sys.argv[1]), total_count=10, skip_status=True)
	for u in users:
		print(u.name)
		print(u.screen_name)
		print(u.id)
		print()
except:
	print("\nCheck your assumptions, beginning with the identity of", str(sys.argv[1]), "who doesn't seem to exist on Twitter.")

