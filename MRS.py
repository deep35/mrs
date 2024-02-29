import pandas as pd
from fuzzywuzzy import process

data = pd.read_csv('20C25015_Deep_Patel.csv',encoding='ISO-8859-1')
# inp=input("Search.......... :")

def search(inp):
    idx1 = process.extractOne(inp, data['artist'])[2]
    artist=data['artist'][idx1]
    if artist.lower()==inp.lower():
        # print('Artist Selected : ', data['artist'][idx1])
        return rec_songs_artist(artist)
    else:
        return search_song(inp)
    
# Searching the songs by artist 

def rec_songs_artist(art):
    art_title=[]
    art_artist=[]
    art_genre=[]
    art_pop=[]

    for i in range(0,574):
        if data['artist'][i]==art:
            art_title.append(data['title'][i])
            art_artist.append(data['artist'][i])
            art_genre.append(data['genre'][i])
            art_pop.append(data['pop'][i])

    art_df=pd.DataFrame()
    art_df['title']=art_title
    art_df['artist']=art_artist
    art_df['genre']=art_genre
    art_df['pop']=art_pop
    # print(art_df.head())
    # print("Recommanded songs by searched artist ..............")
    songs = art_df.nlargest(5,['pop'])
    song_title = songs['title'].tolist()
    song_artist = songs['artist'].tolist()
    recom = []
    for i in range(0,5):
        rec = song_title[i]+" by " +song_artist[i]
        recom.append(rec)

    return recom

# Songs recommandation by searched song 

def search_song(inp):
    idx = process.extractOne(inp, data['title'])[2]
    print('Song Selected : ', data['title'][idx], 'Index : ', idx)
    bpm=data['bpm'][idx]
    pop=data['pop'][idx]
    input_data=[bpm,pop]
    return rec(input_data)

new_data = pd.read_csv('20C25015_Deep_Patel.csv',encoding='ISO-8859-1', usecols=['bpm', 'pop'])
# new_data

columns = list(new_data)

def rec(in_data,k=6):
    data_arr = []
    dist_arr = []

    for i in range(0, 575):
        for j in columns:
            # print(new_data[j][i])
            ele = new_data[j][i]
            data_arr.append(ele)
        # print(data_arr)
        dist = ((in_data[0]-data_arr[0]) ** 2 +(in_data[1]-data_arr[1]) ** 2) ** 0.5
        dist_arr.append(dist)
        data_arr = []

    result = pd.DataFrame(dist_arr)
    result['bpm'] = new_data['bpm']
    result['pop'] = new_data['pop']
    result['title'] = data['title']
    result['artist'] = data['artist']
    result['genre'] = data['genre']

    # print("Recommanded songs by searched song ..............")
    songs = result.nsmallest(k,[0])
    songs_title = songs['title'].tolist()
    songs_title.pop(0)
    songs_artist = songs['artist'].tolist()
    recom = []
    for i in range(0,5):
        rec = songs_title[i]+" by " +songs_artist[i]
        recom.append(rec)

    return recom

# search(inp)