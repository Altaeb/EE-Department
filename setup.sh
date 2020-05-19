#----------------------------------------------------------------------------#
#                                    Auth0
#----------------------------------------------------------------------------#

export AUTH0_DOMAIN = 'altaeb.eu.auth0.com'
export API_AUDIENCE = 'EE-Department'
export ALGORITHMS = ['RS256']

#----------------------------------------------------------------------------#
#                                 DATABASE URL
#----------------------------------------------------------------------------#

export DATABASE_URL = 'postgresql://postgres:1111@localhost:5432/ee-deepartment'
export TEST_DATABASE_URL = 'postgresql://postgres:1111@localhost:5432/ee_deepartment_test'

#----------------------------------------------------------------------------#
#                                 Auth tokens
#----------------------------------------------------------------------------#

export ASSISTANT_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZLUlZGSWwySXpGY0psSjc0R2VzVSJ9.eyJpc3MiOiJodHRwczovL2FsdGFlYi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMjgwZTQ1YzUxZDEwYmU4ZmJlYzc4IiwiYXVkIjoiRUUtRGVwYXJ0bWVudCIsImlhdCI6MTU4OTgwNjgxOCwiZXhwIjoxNTg5ODE0MDE4LCJhenAiOiJ2ekJoTkxPd0JzMERIbk90SGZjdFA1ak1tWHJmc0NObiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnNoZWV0cyIsImdldDpzdWJqZWN0cyJdfQ.dsBkBWjwG-CoI0msOAEocJ7ok_XKpv2UKDnDEaCzcgTcb4NEbm9ctItmJ87lA2C3KSwvcLQg20JlpuZSF6aTZRY6GT5EVkUE8T7qyXhlEE_xeWhhutWya6BgCS9RgclPOGzE3Zb0RZTSFHpdZjBaC03hGd6jQS9kePBaECOM7_KbRlvVFPBlaBg8dObM5RJD5hWchSvdPfaPikEB30ix04Ctsewhd5P8INaNcDgr5sbshcn40zyL7HFQdSnT8xvCjr0CoAxuOV81B3UhOQqTMHNWLev15zqYtcYsO0AvRCcqzlm2oGup6fCmiDO0QbsHbow1ExIHx35xVO1ZDooYeg'

export ASSISTANT_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZLUlZGSWwySXpGY0psSjc0R2VzVSJ9.eyJpc3MiOiJodHRwczovL2FsdGFlYi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMjgxNDM1YzUxZDEwYmU4ZmJlZDJmIiwiYXVkIjoiRUUtRGVwYXJ0bWVudCIsImlhdCI6MTU4OTgwNjYyOCwiZXhwIjoxNTg5ODEzODI4LCJhenAiOiJ2ekJoTkxPd0JzMERIbk90SGZjdFA1ak1tWHJmc0NObiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnNoZWV0cyIsImdldDpzdWJqZWN0cyIsInBhdGNoOnNoZWV0cyIsInBhdGNoOnN1YmplY3RzIiwicG9zdDpzaGVldHMiLCJwb3N0OnN1YmplY3RzIl19.gVkubRQehXXGFW0TlCgG2MSQeho3QNekU8HfYbl3h5WdZbrHUHXzSfVy7ezvU2PN3CEhHKBhZlw_o6OMrGDKLlr92uAAXO48KVzxt4MOEzeNuTDtitDmg2wEl-IxOgzQDNmNJc9VHFytgl_vOSnX-TEAkk2iNwpGq8lGP5MWJ87DlD-BlKptWOE1OfpdA5VDJ5wdttvHvLciufFg1H8bs6vGmCQJQ4WHG6P-TNsSpEpIb919XbyfqLBEYTeGw-dvh5gSeEXNL5FNouEWWYnAor6S9dESDE1r7DnRE3YWhJK1mDDhqZFCsmr4aZ1A-qOGj74qdGVV1mz_fDXMRTFk9A'

export ASSISTANT_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZLUlZGSWwySXpGY0psSjc0R2VzVSJ9.eyJpc3MiOiJodHRwczovL2FsdGFlYi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMjgxYWU4YjIzOWQwYmZlNzBiMTUzIiwiYXVkIjoiRUUtRGVwYXJ0bWVudCIsImlhdCI6MTU4OTgwNjI0NCwiZXhwIjoxNTg5ODEzNDQ0LCJhenAiOiJ2ekJoTkxPd0JzMERIbk90SGZjdFA1ak1tWHJmc0NObiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnNoZWV0cyIsImRlbGV0ZTpzdWJqZWN0cyIsImdldDpzaGVldHMiLCJnZXQ6c3ViamVjdHMiLCJwYXRjaDpzaGVldHMiLCJwYXRjaDpzdWJqZWN0cyIsInBvc3Q6c2hlZXRzIiwicG9zdDpzdWJqZWN0cyJdfQ.I1WlddHg55CqbivHqVkHwdq-LI-NrtAZEPdgmHSjuxkdLiPgARQhpj8bRGfz9wqjG5TY1EbBE6jm-878yN8IsWphx5pXRuDtwZqzSaOdP7ZG4btlU412aJEAou-t_rnolfv095tgcqqKjQnXinutGC2gxnEAdee3P5n9EItBvi3T130HQjZz24zGav0naJzMHrlv7e9-VsLNSoeGn-lONDbXcWfqokTUQMYT00rXnBlych6-5x-LD6uNsO7PZV-51U2jllbBqpidpe4B5mnyYQE7gOrqoSw90ToMz8p5KxEUvIZG0DhA35tBbD3kqAg4ezYaSLyRcFQeZT0-ikTJpQ'
