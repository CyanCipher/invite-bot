import praw
import ids

reddit = praw.Reddit(client_id = ids.CLIENT_ID, client_secret = ids.SECRET_KEY, username= 'Dangerous-Hornet9878', password= ids.PASS, user_agent= 'SandeshVahak')


reddit.redditor("Cyan-Cypher").message(subject="TEST", message="test message from sandeshvahak")