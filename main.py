from modules import url_funcs, url_scraper
import pyfiglet

ascii_banner = pyfiglet.figlet_format('spider')
print(f'{ascii_banner}\nSpareAByte\n\n')

url = input('Enter url: ')

user_wait = input('''
                  How long between requests?
                  (Choose an option)
                  1 : 0s Let the site block me
                  2 : 1s Play it safe
                  3 : 1s-3s random
                  4 : 3s Play it safe
                  ''')


formated_url = url_funcs.verify_url(url)
user_timer = url_funcs.user_timer(user_wait)
url_scraper.scraper(formated_url)
print(', '.join(url_scraper.email_list), url_funcs.timer)
print(user_timer)