from make_request import *
import pandas as pd

def display_stats():

    # Stats sur dbpedia
    print('\nInformation about Dbpedia')
    ## Requete 1 - Stats
    sys.argv[1] = "dbpedia"
    sys.argv[2] = 1
    make_request()
    df = pd.read_csv('temp.csv')
    nbAnime = len(df)
    print("Number of anime : " + str(nbAnime))

    ## Requete 2 - Stats
    sys.argv[2] = 2
    make_request()
    df = pd.read_csv('temp.csv')
    df = df.dropna()
    studio_name = ''
    studio_anime_nb = 0
    current_studio = ''
    current_nb = 0
    for index, row in df.iterrows():
        if(str(row['studio']) == current_studio):
            current_nb+=1
        else:
            if(current_nb > studio_anime_nb):
                studio_anime_nb = current_nb 
                studio_name = current_studio
            else:
                current_nb=1
                current_studio = row['studio']
    df = df['studio'].unique()
    print("Number of studio : " + str(len(df)))
    print("The studio that has the most number of anime : " + studio_name)
    print("It has " + str(studio_anime_nb) + " anime")

    ## Requete 3 - Stats
    sys.argv[2] = 4
    make_request()
    df = pd.read_csv('temp.csv')
    print("Number of original anime : " + str(len(df)) + "\nIt's " + str(round(len(df)/nbAnime * 100)) + "%")
    print("Number of adaptated anime : " + str(nbAnime - len(df)) + "\nIt's " + str(round((nbAnime - len(df))/nbAnime*100)) + "%")
    
    # Stats sur dbpedia
    print('\nInformation about Wikidata')
    ## Requete 1 - Stats
    sys.argv[1] = "wikidata"
    sys.argv[2] = 1
    make_request()
    df = pd.read_csv('temp.csv')
    nbAnime = len(df)
    print("Number of anime : " + str(nbAnime))

    ## Requete 2 - Stats
    sys.argv[2] = 2
    make_request()
    df = pd.read_csv('temp.csv')
    df = df.dropna()
    studio_name = ''
    studio_anime_nb = 0
    current_studio = ''
    current_nb = 0
    for index, row in df.iterrows():
        if(str(row['studioLabel']) == current_studio):
            current_nb+=1
        else:
            if(current_nb > studio_anime_nb):
                studio_anime_nb = current_nb 
                studio_name = current_studio
            else:
                current_nb=1
                current_studio = row['studioLabel']

    df = df['studioLabel'].unique()
    print("Number of studio : " + str(len(df)))
    print("The studio that has the most number of anime : " + studio_name)
    print("It has " + str(studio_anime_nb) + " anime")

    ## Requete 3 - Stats
    sys.argv[2] = 3
    make_request()
    df = pd.read_csv('temp.csv')
    genre_name = ''
    genre_anime_nb = 0
    current_genre = ''
    current_nb = 0
    for index, row in df.iterrows():
        if(str(row['genreLabel']) == current_genre):
            current_nb+=1
        else:
            if(current_nb > genre_anime_nb):
                genre_anime_nb = current_nb 
                genre_name = current_genre
            else:
                current_nb=1
                current_genre = row['genreLabel']


    df = df['genreLabel'].unique()
    print("Number of genre : " + str(len(df)))
    print("The most popular genre : " + genre_name)
