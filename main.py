import pandas as pd
from pyvis.network import Network
import networkx as nx


def init(graph):
    df_ani_stu = pd.read_csv('sparql_data.csv')
    df_stu_gen = pd.read_csv('studio_genres.csv')
    size_stu_gen = len(df_stu_gen.values)
 
    genre_nodes_infos = set_genre_nodes(graph, df_stu_gen, size_stu_gen)
    studio_nodes_info = set_studio_nodes(graph, df_stu_gen, size_stu_gen, genre_nodes_infos)

    size_ani_stu = len(df_ani_stu)
    for i in range(size_ani_stu):
        if studio_nodes_info.get(df_ani_stu.values[i][0]):
            graph.add_node(i + size_ani_stu * 2, size=15, label=df_ani_stu.values[i][1], group=3)  # Anime
            graph.add_edge(studio_nodes_info.get(df_ani_stu.values[i][0]), i + size_ani_stu * 2, weight=3)


def set_studio_nodes(graph, df, size, genre_nodes_info):
    studio_nodes_info = {}
    for i in range(size):
        index_studio = -1
        label = df.values[i][0]
        if not studio_nodes_info.get(label):
            graph.add_node(i + size, size=15, label=label, group=2)  # Studio
            studio_nodes_info[label] = i + size
            index_studio = i + size
        else:
            index_studio = studio_nodes_info.get(label)
        graph.add_edge(genre_nodes_info.get(df.values[i][1]), index_studio, weight=3)
    return studio_nodes_info


def set_genre_nodes(graph, df, size):
    genre_nodes_info = {}
    for i in range(size):
        label = df.values[i][1]
        if not genre_nodes_info.get(label):
            graph.add_node(i, size=15, label=label, group=1)  # Genre
            genre_nodes_info[label] = i
    return genre_nodes_info
 
    
if __name__ == '__main__':
    nx_graph = nx.Graph()
    init(nx_graph)
    
    nt = Network('720','1500')
    nt.from_nx(nx_graph)
    nt.show('index.html')
