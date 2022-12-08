import sys
from display_graph import generate_graph_complete, generate_graph_anime, generate_graph_anime_and_studios,generate_graph_studios_and_genres
from make_request import make_request

def printMenu():
    print("0 - Set src (default ...)")
    print("1 - Display animes (Q1)")
    print("2 - Display studios & animes (Q2)")
    print("3 - Display studios & genres (Q3) /!\ only with wikidata")
    print("4 - Display originals animes for each studio /!\ only with dbpedia")
    print("5 - Display all")
    print("6 - exit")

def execution(numReq : str):
    if numReq == '1' or numReq == '2' or numReq == '3' or numReq == '4':
        sys.argv[2] = numReq

    # Display the graph
    if numReq == '1':
        make_request()
        generate_graph_anime()
        print("anime.html generated\n")
    elif numReq == '2':
        make_request()
        generate_graph_anime_and_studios()
        print("animestudios.html generated\n")
    elif numReq == '3':
        sys.argv[1] = 'wikidata'
        make_request()
        generate_graph_studios_and_genres()
        print("studiogenres.html generated\n")
    elif numReq == '4':
        sys.argv[1] = 'dbpedia'
        make_request()
        generate_graph_anime_and_studios()
        print("animestudios.html generated\n")
    elif numReq == '5': 
        generate_graph_complete()
        print("animestudiogenre.html generated\n")
    
if __name__ == "__main__":
    sys.argv += ['wikidata']
    sys.argv += ['1']
    fin = False
    while not fin :
        printMenu()
        buff = input('>>> ')
        match buff:
            case '0':
                print("Choose between : ")
                print("1 - Wikidata")
                print("2 - Dbpedia")
                buff = input('>>> ')
                if buff == '1':
                    sys.argv[1] = 'wikidata'
                elif buff == '2':
                    sys.argv[1] = 'dbpedia'
                else: pass
            case '1':
               execution('1')
            case '2':
                execution('2')
            case '3':
                execution('3')
            case '4':
                execution('4')
            case '5':
                execution('5') 
            case '6':
                fin = True
            case _:
                pass
        
            
        
        
        
        
    
    
    
    
