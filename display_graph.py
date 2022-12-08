import pandas as pd
from pyvis.network import Network
import networkx as nx


# --- GRAPH ANIME ONLY ---
def generate_graph_anime():
    nx_graph = nx.Graph()
    df = pd.read_csv('temp.csv')
    size = len(df.values)

    for i in range(size):
        nx_graph.add_node(i, size=15, label=df.values[i][0], group=3)
    
    nt = Network('720','1500')
    nt.from_nx(nx_graph)
    nt.show('anime.html')


# --- GRAPH ANIME AND STUDIOS ---
def generate_graph_anime_and_studios():
    nx_graph = nx.Graph()
    df = pd.read_csv('sparql_data.csv')

    size = len(df.values)

    studio_nodes_info = {}
    for i in range(size):
        label = df.values[i][0]
        if not studio_nodes_info.get(label):
            nx_graph.add_node(i, size=15, label=label, group=2)
            studio_nodes_info[label] = i

    for i in range(size):
        if studio_nodes_info.get(df.values[i][0]):
            nx_graph.add_node(i + size, size=15, label=df.values[i][1], group=3)
            nx_graph.add_edge(studio_nodes_info.get(df.values[i][0]), i + size, weight=3)
    
    nt = Network('720','1500')
    nt.from_nx(nx_graph)
    nt.show('animestudios.html')


# --- GRAPH STUDIOS AND GENRES --- 
def generate_graph_studios_and_genres():
    nx_graph = nx.Graph()
    df = pd.read_csv('studio_genres.csv')

    size = len(df.values)

    genre_nodes_infos = _set_genre_nodes(nx_graph, df, size)
    studio_nodes_info = _set_studio_nodes(nx_graph, df, size, genre_nodes_infos)
    
    nt = Network('720','1500')
    nt.from_nx(nx_graph)
    nt.show('studiosgenres.html')


# --- GRAPH ANIME, STUDIOS AND GENRES ---
# Fonction principale : initialise et affiche le graphe dans index.html
def generate_graph_complete():
    df_ani_stu = pd.read_csv('sparql_data.csv')
    df_stu_gen = pd.read_csv('studio_genres.csv')

    nx_graph = nx.Graph()
    _init(nx_graph, df_ani_stu, df_stu_gen)
    
    nt = Network('720','1500')
    nt.from_nx(nx_graph)
    nt.show('animestudiogenre.html')


# Initialise les noeuds et relations du graphe
# Noeuds : Group 1 = Genre, Group 2 = Studio, Group 3 = Anime
def _init(graph, df_ani_stu, df_stu_gen):
    size_stu_gen = len(df_stu_gen.values)
    size_ani_stu = len(df_ani_stu)
 
    genre_nodes_infos = _set_genre_nodes(graph, df_stu_gen, size_stu_gen)
    studio_nodes_info = _set_studio_nodes(graph, df_stu_gen, size_stu_gen, genre_nodes_infos)

    for i in range(size_ani_stu):
        if studio_nodes_info.get(df_ani_stu.values[i][0]):
            graph.add_node(i + size_ani_stu * 2, size=15, label=df_ani_stu.values[i][1], group=3)
            graph.add_edge(studio_nodes_info.get(df_ani_stu.values[i][0]), i + size_ani_stu * 2, weight=3)


# Initialise les noeuds des studios et leurs relations avec les genres
def _set_studio_nodes(graph, df, size, genre_nodes_info):
    studio_nodes_info = {}
    for i in range(size):
        index_studio = -1
        label = df.values[i][0]
        if not studio_nodes_info.get(label):
            graph.add_node(i + size, size=15, label=label, group=2)
            studio_nodes_info[label] = i + size
            index_studio = i + size
        else:
            index_studio = studio_nodes_info.get(label)
        graph.add_edge(genre_nodes_info.get(df.values[i][1]), index_studio, weight=3)
    return studio_nodes_info


# Initialise les noeuds des genres
def _set_genre_nodes(graph, df, size):
    genre_nodes_info = {}
    for i in range(size):
        label = df.values[i][1]
        if not genre_nodes_info.get(label):
            graph.add_node(i, size=15, label=label, group=1)
            genre_nodes_info[label] = i
    return genre_nodes_info

