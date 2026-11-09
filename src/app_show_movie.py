'''
Programming: Python
Author     : AEAhwazi
Date       : 2026/08/13
Project    : Get movies information from API
'''
import streamlit as st
import requests
import fun_get_id

st.title('MOVIES INFORMATION...')

option = st.sidebar.selectbox('Select Your Option: ',
                              ('CALL API BY ID',\
                                'CALL API BY NAME',\
                               'MOVIE LIST BY PAGE',\
                                'MOVIE BY GENRES ID',\
                                'MOVIE BY GENRES NAME'))

if option == 'CALL API BY ID':
    movie_id = st.number_input('Enter movie id, [1-250]: ', min_value=1, max_value=250)
    if st.button('Display Info: '):
        result = fun_get_id.get_Movie_ID(movie_id) #Get data from function and set to result
        if result != 'Error':
            st.success('DATA DISPLAY BELLOW:')
            for key in result:                      #Loop to display information of movie
                st.write(str(key) + ': ' + str(result[key]))
        else:
            st.error('DATA NOT FOUND')

elif option == 'CALL API BY NAME':
    name = st.text_input("Enter name movie: ")
    if st.button("Display Info:"):
        result = fun_get_id.get_Movie_Name(name)    #Get data from function and set to result
        if result != 'Error':
            st.success('DATA DISPLAY BELLOW:')
            v_data = ''
            st.write(result)                        #Display information of movie
            
        else:
            st.error('DATA NOT FOUND!')

elif option == 'MOVIE LIST BY PAGE':
    movie_page = st.number_input('Enter page number, [1-25]: ', min_value=1, max_value=25)
    if st.button('Display Info: '):
        result = fun_get_id.get_Movie_List(movie_page) #Get data from function and set to result
        if result != 'ERROR':
            st.success('DATA DISPLAY BELLOW')
            st.write(result)                           #Display information of movie
        else:
            st.error('DATA NOT FOUND')


elif option == 'MOVIE BY GENRES ID':
    genre_id = st.number_input('Enter Genres ID, [1-21]: ', min_value=1, max_value=21)
    page = st.number_input('Enter page number, [1-25]: ', min_value=1, max_value=25)
    if st.button('Display Info: '):
        result = fun_get_id.get_Movie_Genres_ID(genre_id, page) #Get data from function and set to result
        if result != 'ERROR':
            st.success('DATA DISPLAY BELLOW')
            st.write(result)                                    #Display information of movie
        else:
            st.error('DATA NOT FOUND')

elif option == 'MOVIE BY GENRES NAME':    
    genres_list = fun_get_id.get_Movie_Genres_Name()        #Get genres list from function\
                                                            #and set to genres_list
    #---------------------------Create selectbox of the genres list
    select_genres = st.selectbox("Please select genres of list to view movies:", genres_list)

    genre_id = genres_list.index(select_genres)            #Get index of genres list by name
    genre_id += 1

    url = f'https://moviesapi.ir/api/v1/genres/{genre_id}/movies?page='
    response = requests.get(url)                           #Connect to url

    if response.status_code != 200:
        st.write("Error Website!")

    else:
        genres_movie_dic = response.json()                 #Get data from website
        st.success(f'Id of genre: {genre_id}')
        for i in range(len(genres_movie_dic['data'])):     #Loop to set fields to any variable
            id = genres_movie_dic['data'][i]['id']
            title = genres_movie_dic['data'][i]['title']
            poster = genres_movie_dic['data'][i]['poster']
            genres = genres_movie_dic['data'][i]['genres']
            images = genres_movie_dic['data'][i]['images']
            st.sidebar.image(poster)
        
            st.write('Id: ',id)
            st.write('Title: ',title)
            st.write('Poster: ', poster)
            st.write('Genres: ', genres)
            st.write('Images: ', images)

#End Program.