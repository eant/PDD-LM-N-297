import tweepy
from pprint import pprint

claves = open('C:/Users\gonza\Documents\Trabajo\EANT\Python\claves_twitter.txt')
keys = [clave.strip('\n') for clave in claves]

consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Mi perfil
usuario = api.me()
pprint(usuario.name)
#%%
#Otro usuario
otro_usuario = api.get_user('DrBrianMay')
pprint(otro_usuario.followers_count)
#%%
seguidores = api.followers(screen_name = 'DrBrianMay')
for seguidor in seguidores:
   print(seguidor.name)
#%%
#Si quiero más de 20 resultados
for amigo in tweepy.Cursor(api.friends, screen_name = 'DrBrianMay').items(50):
   nombre = amigo.screen_name
   print(nombre)
#%%
#Los tweets posteados, con los RT
for tweet in tweepy.Cursor(api.user_timeline, screen_name = 'alferdez', tweet_mode = 'extended').items(10):
   if tweet.full_text.startswith("RT @"): texto = tweet.retweeted_status.full_text
   else: texto = tweet.full_text
   print(texto, '\n')
#%%
for tweet in tweepy.Cursor(api.search, q = 'music', tweet_mode = 'extended').items(10):
   print(tweet.full_text, '\n')


