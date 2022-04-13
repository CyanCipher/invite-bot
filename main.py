from rich.console import Console
from halo import Halo
import praw
import ids
import csv
import time

console = Console()

reddit = praw.Reddit(client_id = ids.CLIENT_ID, client_secret = ids.SECRET_KEY, username= 'Dangerous-Hornet9878', password= ids.PASS, user_agent= 'SandeshVahak')

msg = '''Hi

I am very impressed by your profile here. You seems like a great person. I like the way you roll.

Can you please tell me what is your username in bakchodi[dot]org website?? I wanted to follow you up there as I am detoxing from foreign platforms and moving to Indian ones. I don't want to miss your posts and thoughts.

Thank you very much sir. '''


def revisitcheck(usrnm):
    username_exists = False
    with open('sent.csv', 'r') as userchecker:
        csv_reader2 = csv.reader(userchecker)
        for line in csv_reader2:
            try:
                if line[0] == usrnm:
                    username_exists = True
            except:
                pass
    return username_exists


def visitwrite(usrnm):
    with open("sent.csv", "a") as usrlist:
        usrlist.write(usrnm + "\n")


def main():
    with open('tobesent.csv', 'r') as usergetter:
        csv_reader = csv.reader(usergetter)

        for line in csv_reader:
            with Halo(text='...', spinner='dots'):
                raw_line = line[0]
                list_raw_line = list(map(str, raw_line.split(" ")))
                username = list_raw_line[0]
                if not revisitcheck(username):
                    try:
                        reddit.redditor(username).message(subject="Invite", message=msg)
                        visitwrite(username)
                        console.log(f"Sent invite to {username}.", style="bold green")
                        time.sleep(30)
                    except:
                        pass


if __name__=="__main__":
    main()
