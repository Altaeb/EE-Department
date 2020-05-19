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

export ASSISTANT_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZLUlZGSWwySXpGY0psSjc0R2VzVSJ9.eyJpc3MiOiJodHRwczovL2FsdGFlYi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMjgwZTQ1YzUxZDEwYmU4ZmJlYzc4IiwiYXVkIjoiRUUtRGVwYXJ0bWVudCIsImlhdCI6MTU4OTkxNjE3MCwiZXhwIjoxNTg5OTIzMzcwLCJhenAiOiJ2ekJoTkxPd0JzMERIbk90SGZjdFA1ak1tWHJmc0NObiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnNoZWV0cyIsImdldDpzdWJqZWN0cyJdfQ.BGZOz0NA1H9Xa89psVFrOeBNnyrmLe16kamdRf_jU12ydf_QAqBjLGxjUWPr6G0tXxW7ByuINcR0l7oLJtLVxguNdHhFca8WF_3TAh1y0bnwqSamTBrFz0wYkMp_YsgZV2oJetMnyx4crsSelL4ajD_mqeKPbSd8GolEkP-vv1yjasZD_AuzwjYdwOoSpgfnw93c9rfWKLmvYNw6_oBBem9v5ahkUKggneu6vMuz3zgNJF337ARHSCMPitcNM_x69th_0c6QibA8a_pqfV1uZ88BFrjxuw7e7YF5zKbI1uYity5oEum49Jky3cBb_7te_5isU8BiK8VK7lBJ3C-UDw'

export DIRECTOR_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZLUlZGSWwySXpGY0psSjc0R2VzVSJ9.eyJpc3MiOiJodHRwczovL2FsdGFlYi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMjgxNDM1YzUxZDEwYmU4ZmJlZDJmIiwiYXVkIjoiRUUtRGVwYXJ0bWVudCIsImlhdCI6MTU4OTkxNjA0OSwiZXhwIjoxNTg5OTIzMjQ5LCJhenAiOiJ2ekJoTkxPd0JzMERIbk90SGZjdFA1ak1tWHJmc0NObiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnNoZWV0cyIsImdldDpzdWJqZWN0cyIsInBhdGNoOnNoZWV0cyIsInBhdGNoOnN1YmplY3RzIiwicG9zdDpzaGVldHMiLCJwb3N0OnN1YmplY3RzIl19.UD2w7NqMn9iZDoEm04N0cQc5nYrA4Up68Xar2RTvOdXEeJCqU8S0Ptukbh1xHPt_VXFo_KCH7sMLv_CmM4MbEJU_kIE7sggXGPbP7CarJDJpGjdjl4idUbYqw_xNzmV0vcOnuLfBwKu40M-uVIbGUgOMrZy9TZRExw47MTdVx0c6wYrBvdvi17x18lSc_FgbIGBrTLxTSJuG9mVMr--FzYq-sxohCyBoaAQTIH7W2xgzYDecRGEyzEAOi3l83il7tpA8e0If6KAcsfsSf8z2mV0hOnOLJ1tXIug8GhtcNhuW526vD_LI8-Bsg0r6J8bwHlyKnkP7_v6L0nmVMjZYOQ'

export PRODUCER_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZLUlZGSWwySXpGY0psSjc0R2VzVSJ9.eyJpc3MiOiJodHRwczovL2FsdGFlYi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMjgxYWU4YjIzOWQwYmZlNzBiMTUzIiwiYXVkIjoiRUUtRGVwYXJ0bWVudCIsImlhdCI6MTU4OTkxNDg4MSwiZXhwIjoxNTg5OTIyMDgxLCJhenAiOiJ2ekJoTkxPd0JzMERIbk90SGZjdFA1ak1tWHJmc0NObiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnNoZWV0cyIsImRlbGV0ZTpzdWJqZWN0cyIsImdldDpzaGVldHMiLCJnZXQ6c3ViamVjdHMiLCJwYXRjaDpzaGVldHMiLCJwYXRjaDpzdWJqZWN0cyIsInBvc3Q6c2hlZXRzIiwicG9zdDpzdWJqZWN0cyJdfQ.dfyt1A8otVr2ykmuy1uwRQOfzCBFwNT3QtxU6HyKiM2qm-PBe_Z-aazwS7JWVvw8IUTvnC1r0KVfbA7mUaH93wbg2Kc26vnAKuwIewt0x3ATldsN1tXrXCPmrGqsC4l7H-rT7ZV_wd0I3vPBR3J-z-xYZRKh5az1qEmc_jgrX0savWOUPf2_0JhaPSYGeBieNw_87NL1nlHHtYXT8G_XJkloUiJXT_6u5lruXctSjKhFzxyk7XUk4qG9LJ_pPrMm_WAOWIo8Pq38-zJ5UAy77TJDLnBq-CRwJghID3rNZuAqKEaC9PqEYPEsHTVc1-PDhPYIN2ehgUww1oZ-q_qlLQ'
