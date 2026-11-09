'''
Programming: Python
Author     : AEAhwazi
Date       : 2026/08/13
Project    : Functions Get movies information from API
'''
import requests
import os

def get_Movie_ID(movie_id):
    url = f"https://moviesapi.ir/api/v1/movies/{movie_id}"

    response = requests.get(url)
    if response.status_code != 200:
        return 'Error'
    else:
        response = response.json()

        return response
#*************************************************************

def get_Movie_Name(name, page=1):
    url = f"https://moviesapi.ir/api/v1/movies"
    mydict = {'q':name, 'page':page}
    respons = requests.get(url, params=mydict)
    if respons.status_code != 200:
        return 'Error'

    else:
        respons = respons.json()
        return respons
#*************************************************************

def get_Movie_List(page=1):
    url = f"https://moviesapi.ir/api/v1/movies"
    mydic = {'page' : page}
    response = requests.get(url, params=mydic)

    if response.status_code != 200:
        return 'Error'

    else:
        output = []
        response = response.json()
        response = response['data']

        for item in response:
            title = item['title']
            poster = item['poster']
            imdb_rating = item['imdb_rating']
            year = item['year']
            output.append([title, poster, imdb_rating, year])
#*************************************************************

        return output

def get_Movie_Genres_ID(genre_id, page):
    url = f"https://moviesapi.ir/api/v1/genres/{genre_id}/movies?page={page}"
    #url = f"https://moviesapi.ir/api/v1/genres"
    #mydic = {'genre_id': genre_id, 'page' : page}
    #response = requests.get(url, params=mydic)
    response = requests.get(url)

    if response.status_code != 200:
        return 'Error'

    else:
        output = response.json()

        return output
       
#*************************************************************
def get_Movie_Genres_Name():
    #------------------------------Create list for genres names
    genres_list = []

    #------------------------------Link of movies website
    url = f"https://moviesapi.ir/api/v1/genres"

    #------------------------------Get responsing data of website
    response = requests.get(url)
    if response.status_code != 200:
        return "Error"

    else:
        genres_dic = response.json()

        #---------------------------Loop for add genres names to list
        for item in genres_dic:
            genres_list.append(item['name'])

        return genres_list

#End Functions
