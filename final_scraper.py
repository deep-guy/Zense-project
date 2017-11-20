#! /usr/bin/env python
import requests
import urllib3
import os
from datetime import datetime
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
current_time = map(str, str(datetime.now()).split('.'))[0]

display_file_path = ""  #Enter the path for an extra file
output_file_path = ""   #Enter the path for the file that will get updated
def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
checker = 0
if (is_non_zero_file("/home/deepinder/Desktop/WebScr/Output.txt") == False):
    with open("/home/deepinder/Desktop/WebScr/Output.txt", "w") as writer:
        writer.write("")
    checker = 1

USERNAME = ''   #Enter your lms username
PASSWORD = ''   #Enter your lms password
url = "https://lms.iiitb.ac.in/moodle/login/index.php"
payload = {"username" : USERNAME  , "password" : PASSWORD}
import sys

reader = open(display_file_path, "r")
lines = reader.readlines()
reader.close()
with open(display_file_path, "w") as clearer:
    clearer.write("")
if (checker == 1):
    with open(output_file_path, "a") as updates:
        updates.write("This is the first execution\n")
page_soup = ""
forum_flag = 0
with requests.Session() as c:
#Session starts a session with the page, which takes care of cookies
    #.post command posts the log in info
    #I have set ssl certificate verification to false
    #for some reason, i dont have the certificates.
    #this is a quick workaround to this problem
    c.post(url, data = payload, verify = False)
    #getting all html codes from the link
    r = c.get("https://lms.iiitb.ac.in/moodle/my/")
    #converting them to readable text
    words = r.text
    #have installed the lxml parser
    soup = BeautifulSoup(words, "lxml")
    course_box_list = soup.findAll("div", {"class":"box coursebox"})
    links_list = []
    title_list = []
    events_list = soup.findAll("div", {"class":"event"})

    for course_box in course_box_list:
        if (course_box.findAll("div", {"class": "activity_info"}) != []):
            title_list.append(course_box.div.h2.a["title"])
            links_list.append(course_box.div.h2.a["href"])
    new_subject_flag = 0

    if (len(links_list) > len(lines)):
        for i in xrange(len(links_list) - len(lines)):
            lines.append("")
        new_subject_flag = 1
    counter = 0
    Flag = 0
    for i in xrange(len(links_list)):
        
        page = c.get(links_list[i])
        page_html = page.text
        page_soup = BeautifulSoup(page_html, "lxml")
        forum_list = page_soup.findAll("div", {"class":"activityhead"})
        recent_link = ""

        #Block to get a link of recent activity of forum posts
        for l in forum_list:
            if (l.a != None):
                if(l.a.text == "Full report of recent activity..."):    
                    recent_link = l.a["href"]

        #Checking for new assignments
        all_names = []
        flag = 0
        all_names_html = page_soup.findAll("span", {"class":"instancename"})
        list_file = []
        for x in range(len(lines)):
            list_file.append("")
        for j in all_names_html:
            if(len(list_file) > i):
                list_file[i] += str(j.text).strip() + "|"
                counter += 1
            else:
                list_file.append(str(j.text).strip() + "|")
                counter += 1


        if (checker == 0):
            lists_ele = map(str, str(lines[i]).strip().split("|"))
            list_file_ele = map(str, list_file[i].strip().split("|"))
            for q in list_file_ele:
                if (q not in lists_ele and new_subject_flag != 1):
                    with open(output_file_path, "a") as updates:
                        updates.write(current_time + "  New Assignment update for " + str(title_list[i]) + ":  " + q + "\n")
                        Flag = 1
            if(new_subject_flag == 1):
                with open(output_file_path, "a") as updates:
                    updates.write(current_time + "  New Assignment update for " + str(title_list[i]) + ":  " + list_file_ele[len(list_file_ele) - 1])
                    Flag = 1
            
        with open(display_file_path, "a") as writer:
            for item in list_file:
                writer.write(item)
            writer.write("\n")
        
        
        #Checking for new forum posts.
        page = c.get(recent_link)
        page_html = page.text
        page_soup = BeautifulSoup(page_html, "lxml")
        replies_list = page_soup.findAll("td", {"class":"reply"})
        posts_list = page_soup.findAll("div", {"class":"discussion"})
        if (replies_list == [] and posts_list == []):
            pass
        else:
            forum_flag = 1
            with open(output_file_path) as updates:
                updates.write(current_time +":  There are new forum posts by:-\n")
                for r in posts_list:
                    x = r.findAll('div', {"class":"user"})
                    print x
                    for y in x:
                        updates.write(y.a.text + "|    ")
                updates.write("\n")
        


    if(Flag == 0):
        if (checker == 0):
            with open(output_file_path, "a") as updates:
                updates.write(current_time + ": No new updates for assignments\n")
        else:
            with open(output_file_path, "a") as updates:
                updates.write(current_time + ":  Upcoming events!\n")
                for event in events_list:
                    updates.write(event.a.text + "----")
                    updates.write(event.div.a.text + "\n")
        
                    
                
    if (forum_flag == 0):
        with open(output_file_path, "a") as updates:
            updates.write(current_time + ":  No new forum posts\n")


with open(output_file_path, "a") as updates:
    updates.write('\n')


