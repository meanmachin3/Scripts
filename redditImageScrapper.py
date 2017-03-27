import praw
import platform
import requests
import shutil
import os
import re
try:
    import pwd
except:
    pass
    
def sanitize(link):
    if 'jpg' in link or 'png' in link:
        return link
    elif 'imgur' in link:
        return link + '.png'
    else:
        raise ValueError('cant sanitize url : ' + link)

def main():
    reddit = praw.Reddit(client_id='SDigpqbQpRbdgg',
                     client_secret='Ec-SZ4Fgyeo0FzvD03JVb2CwyNo',
                     password='16071994',
                     user_agent='testscript by /u/_meanmachine_',
                     username='_meanmachine_');
    subreddit = reddit.subreddit('alexandradaddario');
    submissions = []
    for submission in subreddit.top(limit=None):
        submissions.append(submission)   # Output: the URL the submission points to

    my_dir = "C:\\Users\\meanmachine\\Desktop\\Alexandra";

    if not os.path.exists(my_dir):
        os.makedirs(my_dir)

    i = 0
    for submission in submissions:
        each = submission
        try:
            url = sanitize(each.url)
            imgext = url.split('.')[-1]
            title = each.title
        except ValueError as e:
            print (e)
            i += 1
            continue
        title = re.sub(r'[^\w]', ' ', title)
        imgext = re.sub(r'[^a-zA-Z]+', ' ', imgext)
        print ("Fetching " + title + " " + url)
        if not os.path.exists(my_dir + '\\' + title + '.' + imgext):
            try:
                response = requests.get(url, stream=True)
            except requests.exceptions.ConnectionError as e:
                print (e)
                i += 1
                continue
            with open(my_dir + '\\' + title + '.' + imgext, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

        i += 1

if __name__ == '__main__':
    main()