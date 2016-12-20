#ver .03

from python import requests
import pickle


class UserAuth():
    def __init__(self, login=None, password=None):
        self.login = login
        self.url_json = 'https://park.mail.ru'
        self.password = password
        self.s = requests.Session()
        self.indexUrl = 'https://park.mail.ru/pages/index/'
        self.urlLogin = 'https://park.mail.ru/login/'
        self.urlLogin2 = 'https://park.mail.ru/gtp_login/'
        self.urlLogout = 'https://park.mail.ru/logout/'
        self.urlFeed = 'https://park.mail.ru/feed/subscribed/'
        resp = self.s.get(self.indexUrl)
        self.csrf_token = resp.cookies["csrftoken"]
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
            'Connection': 'keep-alive',
            'Host': 'park.mail.ru', 'Upgrade-Insecure-Requests': "1",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
            'Referer': 'https://park.mail.ru/pages/index/'
        }
        self.headersnew = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
            'Connection': 'keep-alive',
            'Content - Length': '117',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'park.mail.ru',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
            'Referer': 'https://park.mail.ru/pages/index/',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def save_cookies(self, requests_cookiejar, filename):
        with open(filename, 'wb') as f:
            pickle.dump(requests_cookiejar, f)

    def load_cookies(self, filename):
        try:
            with open(filename, 'rb') as f:
                s = pickle.load(f)
                return s
        except:
            return self.s.cookies

    def exit(self):
        return(self.s.post(self.urlLogout))

    def authorization(self):
        self.s.cookies = self.load_cookies('./cookie.txt')
        if (self.s.get(self.urlFeed)).url == self.urlFeed:
            return True
        self.s.headers = self.headersnew

        r = self.s.post(self.urlLogin,
                        {'login': self.login, 'password': self.password,
                         'csrfmiddlewaretoken': self.csrf_token, 'remember': 'on'})
        rnew = self.s.post(self.urlLogin2,
                           {'login': self.login, 'password': self.password,
                            'csrfmiddlewaretoken': self.csrf_token, 'remember': 'on'})

        if (self.s.get(self.urlFeed)).url == self.urlFeed:
            self.save_cookies(r.cookies, './cookie.txt')
            return True
        return False
