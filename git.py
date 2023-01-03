import json 
import requests
import time
from flask import request



def git_api():
        serchfor = request.form.get('rank_git')
        serchfor = str(serchfor)
        serchfor_language = request.form.get('rank_lauguage')
        url = 'https://api.github.com/search/repositories?q=stars%3A%3E1+created%3A' + serchfor + '+language%3A'+ serchfor_language + '&type=Repositories&ref=advsearch&l=&l='
        response = requests.get(url)
        data = json.loads(response.text)
        api_lists = []
        i = 0
        while i < 5:
            
            ranks = [['第' + str(i + 1) + '位   ユーザー名: ' + data.get('items')[i].get('name')],['スター獲得数:  ' + str(data.get('items')[i].get('stargazers_count'))]]
            time.sleep(2)
            i += 1
            ranks = str(ranks).replace('[','').replace(']','')
            ranks = str(ranks).replace('\'','').replace('\'','')
            api_lists.append(ranks)  
        return api_lists
    
def link_url():
        serchfor = request.form.get('rank_git')
        serchfor = str(serchfor)
        serchfor_language = request.form.get('rank_lauguage')
        url = 'https://api.github.com/search/repositories?q=stars%3A%3E1+created%3A' + serchfor + '+language%3A'+ serchfor_language + '&type=Repositories&ref=advsearch&l=&l='
        response = requests.get(url)
        data = json.loads(response.text)
        api_url = []
        
        i = 0
        while i < 5:
            
            url_links =[[str(data.get('items')[i].get('html_url'))]]
            time.sleep(2)
            i += 1
            url_links = str(url_links).replace('[','').replace(']','')
            url_links = str(url_links).replace('\'','').replace('\'','')
            api_url.append(url_links)
        return api_url
            


  

            
           
        

