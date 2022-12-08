
# Get the querry depending on the source and the number
def get_querry(source, num):
    if(source == 'wikidata'):
        if(num == 1):
            # Return la querry wikidata pour avoir tous les animes
            return wikidata_anime()
        if(num == 2):
            # Return la querry wikidata pour avoir tous les animes et leurs studios
            return wikidata_anime_studio()
        if(num == 3):
            # Return la querry wikidata pour avoir tous les studios et les genres des animes qu'ils ont produit
            return wikidata_anime_genre()
    else:
        if(num == 1):
            # Return la querry dbpedia pour avoir tous les animes
            return dbpedia_anime()
        if(num == 2):
            # Return la querry dbpedia pour avoir tous les animes et leurs studios
            return dbpedia_anime_studio()
        if(num == 3):
            # Return la querry dbpedia pour avoir tous les studios et leurs animes originaux 
            return dbpedia_anime_genre()
    return "Error"

# 1 request dbpedia
def dbpedia_anime():
    return '''
        SELECT distinct ?name
        WHERE {
        ?x rdf:type dbo:Anime;
            dbp:name ?name.
        }
        Order by ?anime
    '''

# 2 request dbpedia
def dbpedia_anime_studio():
    return '''
        SELECT distinct ?studio ?anime
        WHERE {
        ?x rdf:type dbo:Company;
            dbo:wikiPageWikiLink ?y.
        ?y dbo:industry dbr:Anime;
            dbo:wikiPageWikiLink ?z;
            dbp:name ?studio.
        ?z rdf:type dbo:Anime;
            dbp:name ?anime.
        }
        Order by ?studio ?anime
    '''

# 3 request dbpedia
def dbpedia_anime_genre():
    return '''
    SELECT distinct ?studio ?anime
    WHERE {
    ?x rdf:type dbo:Company;
        dbo:wikiPageWikiLink ?y.
    ?y dbo:industry dbr:Anime;
        dbo:wikiPageWikiLink ?z;
        dbp:name ?studio.
    ?z rdf:type dbo:Anime;
        dct:subject dbc:Anime_with_original_screenplays;
        dbp:name ?anime.
    }
    Order by ?studio ?anime
    '''

# 1 request wikidata
def wikidata_anime():
    return '''
        SELECT Distinct ?animeLabel
        WHERE
        {
                {?anime wdt:P31 wd:Q63952888.} #Est une serie animation japonaise
            UNION
                {?anime wdt:P31 wd:Q1107.} #Est un anime
            UNION
                {?anime wdt:P31 wd:Q100269041.} #Est une Saison de série d'animation japonaise                    
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } #Pour avoir le label en fr ou sinon en EN si y'en a un
        }
    '''

# 2 request wikidata
def wikidata_anime_studio():
    return '''
        SELECT Distinct ?studioLabel ?animeLabel
    	WHERE
    	{
        	#Doit etre une instance d'un Studio animation japonaise
        	?studio wdt:P31 wd:Q1107679. #Doit etre une instance d'un studio
        	?studio wdt:P452 wd:Q2575347. #Doit etre de l'industrie anime japonaise

        	{?anime wdt:P31 wd:Q63952888.} #Est une serie animation japonaise
        	UNION
            	{?anime wdt:P31 wd:Q1107.} #Est un anime
        	UNION
            	{?anime wdt:P31 wd:Q100269041.} #Est une Saison de série d'animation japonaise 
        	?anime wdt:P272 ?studio. #Pour chaque anime affiche sa societe de production par rapport au studio du dessus
        	SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } #Pour avoir le label en fr ou sinon en EN si y'en a un
    	}
    '''

# 3 request wikidata
def wikidata_anime_genre():
    return '''
        SELECT Distinct ?studioLabel ?genreLabel
        WHERE
        {
            #Doit etre une instance d'un Studio animation japonaise
            ?studio wdt:P31 wd:Q1107679. #Doit etre une instance d'un studio
            ?studio wdt:P452 wd:Q2575347. #Doit etre de l'industrie anime japonaise
                {?anime wdt:P31 wd:Q63952888.} #Est une serie animation japonaise
            UNION
                {?anime wdt:P31 wd:Q1107.} #Est un anime
            UNION
                {?anime wdt:P31 wd:Q100269041.} #Est une Saison de série d'animation japonaise 
            ?anime wdt:P272 ?studio. #Pour chaque anime affiche sa societe de production par rapport au studio du dessus
            ?anime wdt:P136 ?genre. #Un anime possède le genre ?genre (donc donne tous les genres)
                    
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".
                                    ?genre rdfs:label ?genreLabel.
                                    ?studio rdfs:label ?studioLabel.} #Pour avoir le label en fr ou sinon en EN si y'en a un
        }
        ORDER BY ?studioLabel
    '''