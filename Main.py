import twitter

CONSUMER_KEY = 'prjiNXa8WHL5IOS4HNdnqxQRL'
CONSUMER_SECRET = 'hHQ2OJeI26tpHhooihfBvwZ6jNXrlME3DCOKsoaFPKHnaHVhZt'
ACCESS_KEY = '837807691414274051-WMs9arq1V4SHo4mXWgG6YLaDhNbyyKM'
ACCESS_SECRET = 'Cm8aWMQSQVEtlzR8nEXYEBZl2vtS6O4mj0dXdz0yQNyzV'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_KEY,
                  access_token_secret=ACCESS_SECRET)

def getAPI():
    return api
