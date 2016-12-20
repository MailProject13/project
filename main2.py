# coding: utf-8
__version__ = '1.0'
import os
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from python.W_auth_class import UserAuth
from python import W_parser

from kivy.uix.tabbedpanel import TabbedPanel

UAS=UserAuth()


class InterfaceScreen(Screen):

    def __init__(self, **kwargs):
        super(InterfaceScreen, self).__init__(**kwargs)
       # self.sub=True
        self.n=True
        self.sch=True
        self.m=True
        global UAS

    #def download_subscribed(self):
        #if(self.sub):
          #  self.subscribed=W_parser.parse_news(html=W_parser.get_html('https://park.mail.ru/feed/subscribed/', UAS=UAS))
          #  self.ids.first_subscribed_title.text=self.subscribed[0].title
           # self.ids.first_subscribed_info.text=self.subscribed[0].info
           # self.ids.first_subscribed_text.text = self.subscribed[0].text
           # self.ids.first_subscribed_time.text = self.subscribed[0].time
           # self.ids.first_subscribed_author.text = self.subscribed[0].author
          #  self.ids.second_subscribed_title.text = self.subscribed[1].title
           # self.ids.second_subscribed_info.text = self.subscribed[1].info
          #  self.ids.second_subscribed_text.text = self.subscribed[1].text
          #  self.ids.second_subscribed_time.text = self.subscribed[1].time
          #  self.ids.second_subscribed_author.text = self.subscribed[1].author
          #  self.sub=False


    def download_friends(self):
        self.friends=W_parser.parse_friends(html=W_parser.get_html(self.me.href, UAS=UAS))

    def download_me(self):
        if(self.m):
            self.me=W_parser.parse_user(html=W_parser.get_html('https://park.mail.ru/feed/', UAS=UAS))
            self.m=False

    def download_news(self):
        if(self.n):
            self.news=W_parser.parse_news(html=W_parser.get_html('https://park.mail.ru/feed/', UAS=UAS))
            self.ids.first_news_title.text=self.news[0].title
            self.ids.first_news_info.text=self.news[0].info
            self.ids.first_news_text.text=self.news[0].text
            self.ids.first_news_time.text=self.news[0].time
            self.ids.first_news_author.text=self.news[0].author
            self.n=False

    def download_schedule(self):
        if(self.sch):
            self.schedule=W_parser.parse_timetable(html=W_parser.get_html('https://park.mail.ru/feed/', UAS=UAS),UAS=UAS)
            self.ids.first_data.text=self.schedule[0].name
            self.ids.first_day.text = self.schedule[0].date
            self.ids.first_place.text = self.schedule[0].classroom
            self.ids.first_teacher.text = self.schedule[0].teacher
            self.ids.first_time.text = self.schedule[0].time
            self.ids.second_data.text = self.schedule[1].name
            self.ids.second_day.text = self.schedule[1].date
            self.ids.second_place.text = self.schedule[1].classroom
            self.ids.second_teacher.text = self.schedule[1].teacher
            self.ids.second_time.text = self.schedule[1].time
            self.ids.third_data.text = self.schedule[2].name
            self.ids.third_day.text = self.schedule[2].date
            self.ids.third_place.text = self.schedule[2].classroom
            self.ids.third_teacher.text = self.schedule[2].teacher
            self.ids.third_time.text = self.schedule[2].time
            self.ids.fourth_data.text = self.schedule[3].name
            self.ids.fourth_day.text = self.schedule[3].date
            self.ids.fourth_place.text = self.schedule[3].classroom
            self.ids.fourth_teacher.text = self.schedule[3].teacher
            self.ids.fourth_time.text = self.schedule[3].time
            self.ids.fifth_data.text = self.schedule[4].name
            self.ids.fifth_day.text = self.schedule[4].date
            self.ids.fifth_place.text = self.schedule[4].classroom
            self.ids.fifth_teacher.text = self.schedule[4].teacher
            self.ids.fifth_time.text = self.schedule[4].time
            self.ids.sixth_data.text = self.schedule[5].name
            self.ids.sixth_day.text = self.schedule[5].date
            self.ids.sixth_place.text = self.schedule[5].classroom
            self.ids.sixth_teacher.text = self.schedule[5].teacher
            self.ids.sixth_time.text = self.schedule[5].time
            self.sch=False

    def download_messages(self):
        pass


class LoginScreen(Screen):

    def comeIn(self):
        global UAS
        UAS.login = self.login
        UAS.password = self.passwd
        return(UAS.authorization())

    def test_page(self):
        with open('page.html', 'w') as file:
            file.write(W_parser.get_html(UAS.urlFeed, UAS))

class SettingsScreen(Screen):

    def changeuser(self):
        try:
            global UAS
            UAS.exit()
            UAS=None
            return 0
        except:
            return 1



class MainApp(App):
    # create the application screens
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='LoginScreen'))
        self.sm.add_widget(InterfaceScreen(name='InterfaceScreen'))
        self.sm.add_widget(SettingsScreen(name='SettingsScreen'))
        return self.sm



if __name__=='__main__':
    MainApp().run()
