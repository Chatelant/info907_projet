
def get_querry(source, num):
    if(source == 'wikidata'):
        if(num == 1):
            return wikidata_anime()
        if(num == 2):
            return wikidata_anime_studio()
        if(num == 3):
            return wikidata_anime_genre()
    else:
        if(num == 1):
            return dbpedia_anime()
        if(num == 2):
            return dbpedia_anime_studio()
        if(num == 3):
            return dbpedia_anime_genre()
    return "Error"

def dbpedia_anime():
    return '''
        SELECT distinct ?name
        WHERE {
        ?x rdf:type dbo:Anime;
            dbp:name ?name.
        }
        Order by ?anime
    '''

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

def wikidata_anime():
    return '''
        SELECT Distinct ?animeLabel
        WHERE
        {
            {?anime wdt:P31 wd:Q63952888.} #est une serie animation japonaise
            UNION
                {?anime wdt:P31 wd:Q1107.}# est un anime
            UNION
                {?anime wdt:P31 wd:Q100269041.}# Saison de série d'animamation japonaise                    
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # le label viendra de préférence dans votre langue, et autrement en anglais
        }
    '''

def wikidata_anime_studio():
    return '''
        SELECT Distinct ?studioLabel ?animeLabel
    	WHERE
    	{
        	#doit etre une instance d'un Studio animation
        	?studio wdt:P31 wd:Q1107679. # doit etre une instance d'un studio
        	?studio wdt:P452 wd:Q2575347. # doit etre de l'industrie anime japonaise
        	{?anime wdt:P31 wd:Q63952888.} #est une serie animation japonaise
        	UNION
            	{?anime wdt:P31 wd:Q1107.}# est un anime
        	UNION
            	{?anime wdt:P31 wd:Q100269041.}# Saison de série d'animamation japonaise
        	?anime wdt:P272 ?studio. # pour chaque anime affiche sa societe de production par rapport au studio du dessus
        	SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". } # le label viendra de préférence dans votre langue, et autrement en anglais
    	}
    '''

def wikidata_anime_genre():
    return '''
        SELECT Distinct ?studioLabel ?genreLabel
        WHERE
        {
            #doit etre une instance d'un Studio animation
            ?studio wdt:P31 wd:Q1107679. # doit etre une instance d'un studio
            ?studio wdt:P452 wd:Q2575347. # doit etre de l'industrie anime japonaise
                {?anime wdt:P31 wd:Q63952888.} #est une serie animation japonaise
            UNION
                {?anime wdt:P31 wd:Q1107.}# est un anime
            UNION
                {?anime wdt:P31 wd:Q100269041.}# Saison de série d'animamation japonaise
            ?anime wdt:P272 ?studio. # pour chaque anime affiche sa societe de production par rapport au studio du dessus
            ?anime wdt:P136 ?genre. #un anime est de genre * (donc donne tous les genres)
                    
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".
                                    ?genre rdfs:label ?genreLabel.
                                    ?studio rdfs:label ?studioLabel.} # le label viendra de préférence dans votre langue, et autrement en anglais
        }
        ORDER BY ?studioLabel
    '''