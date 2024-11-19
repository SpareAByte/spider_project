import random

# Function used to check format and properly use http is necessary.
def verify_url(url):
    if '://' not in url:
        url = 'https://' + url
        
    if not url.startswith('www.'):
        url = url.replace('://', '://www.', 1)
        
    return url

#Establishing time wait choice
def user_timer(user_wait):
    timer = 0 
    user_wait = int(user_wait)
    if user_wait == 2:
        timer = 1
    elif user_wait == 3:
        timer = random.randint(0, 3)
    elif user_wait == 4:
        timer = 3

    return timer