#ver .03
import json
from python.W_friends_class import Friends
from python.W_timetable_class import Timetable
from python.W_user_class import User
from python.W_news_class import News
from bs4 import BeautifulSoup

def parse_user(html):
    soup = BeautifulSoup(html, "html.parser")
    div_user = soup.find("div", {"class" : "dropdown-user"} )
    u = User()
    u.href = div_user.a["href"]
    u.name = div_user.find("div",{"class":"full_name"}).a.text
    u.picture = div_user.a.img["src"]
                           
    li_f = soup.find_all('li', class_ = "profile__friends-list-item")
    for i in li_f:
        u.friends.append({
            'Friend': i.a.text,
            'Href': i.a["href"],
            'Picture': i.a.img["src"]
            })
    return u
                           
def parse_news(html):
    soup = BeautifulSoup(html, "html.parser")
    news = []
    articles = soup.find_all("article", class_ = "topic topic-type-topic js-topic" )

    for ar in articles:
        news_i = News()
        news_i.title = ar.header.h1.a.text
        news_i.title_href = ar.header.h1.a["href"]
        news_i.info = ar.header.div.text
        news_i.info_href = ar.header.div.a["href"]
        news_i.text = ar.find("div", {"class" : "cf"}).find("div", {"class" : "topic-content text"}).text
        news_i.author = ar.footer.find("li",{"class":"topic-info-author"}).find("a",{"rel":"author"}).text
        news_i.author_href = ar.footer.find("li",{"class":"topic-info-author"}).find("a",{"rel":"author"})["href"]
        news_i.time = ar.footer.find("li",{"class":"topic-info-date"}).span.text
        news.append(news_i)
    return news

def parse_friends(html):
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", {"class" : "dropdown-user"})
    li_f = soup.find_all('li', class_ = "profile__friends-list-item")
    friends = []
    for i in li_f:
        friends_i = Friends()
        friends_i.friend = i.a["title"]
        friends_i.friend_href = i.a["href"]
        friends_i.friend_picture = i.a.img["src"]
        friends.append(friends_i)
    return friends

def parse_timetable(html, UAS):
    soup = BeautifulSoup(html, "html.parser")
    timetable = []
    lessons = soup.find_all("div", class_="schedule-date schedule-date_active js-schedule-date")
    for i in lessons:
        timetable_i = Timetable()
        timetable_i.date = i.find("div", {"class": "schedule-date__value"}).text
        url_json = i.find("div", {"class": "schedule-item js-schedule-item"})

        if url_json != None:
            timetable_i.url_json = url_json["data-url"]
            json_str = get_html((UAS.url_json + timetable_i.url_json), UAS)
            json_dict = json.loads(json_str)
            timetable_i.time = json_dict.get('start_time')
            timetable_i.name = json_dict.get('discipline')
            timetable_i.teacher = json_dict.get('tutor_name')
            timetable_i.classroom = json_dict.get('place')
        else:
            timetable_i.time = ""
            timetable_i.name = "нет занятий"
            timetable_i.teacher = ""
            timetable_i.classroom = ""

        timetable.append(timetable_i)
    return timetable

def get_html(url,UAS):
    response = UAS.s.get(url)
    return response.text

            
     
        
        

   
     
           
