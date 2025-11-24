#Author: Willa Galipeau-Eldridge
#Date: 11/23/2025
#Purpose: HW5: Hash Something Out; Hash Tables

import time
import csv
import re
from datetime import datetime

class DataItem:
    def __init__(self, row):
        self.movie_title = row[0].strip()
        self.genre = row[1].strip()
        self.release_date = datetime.strptime(row[2].strip(), '%m/%d/%Y').date()
        self.director = row[3].strip()
        revenue_str = row[4].strip()
        self.box_office_revenue = float(re.sub(r'[$,]', '', revenue_str))
        self.rating = float(row[5].strip())
        self.duration_minutes = int(row[6].strip())
        self.production_company = row[7].strip()
        self.quote = row[8].strip()
        pass

def hashFunction(stringData):
    #do things to stringData, turn it into an int
    #return key
    key = 0
    #if stringData is none return
    if not stringData:
         return 0
    for character in stringData:
        key += ord(character)
    return key #go through each charater in stringData converting them into an int

def hashPolynomialRolling(stringData):
    if not stringData:
        return 0
    poly = 131 #polynomial bae
    primeMod = int(1e9 +7) #large prime modulus

    key = 0
    pPow = 1

    for character in stringData:
        key = (key + (ord(character)+1) * pPow) % primeMod
        pPow = (pPow * poly) % primeMod
    return key


def buildHashTables(function):  
    #Create an empty Hash Table
    size = 16000
    movies = []
    counter = 0

    #Load the movie data from the provided input file
    file = "MOCK_DATA.csv"
    with open(file, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        #skip the first row that contains column names
        header = next(reader, None)

        for row in reader:
            if (counter == 0):
                counter += 1
                continue
            #print(row)
            #create a DataItem from row
            movie = DataItem(row)
            movies.append(movie)
            #Parse the data to extract movie titles and quotes
            counter += 1

    #Hash Table 1: Movie Title as Key
    #This hash table will use the movie title to store
    #and retrieve movie records.
    startTitle = time.time() #start time to record for title hash table
    hashTitleTable = [None] * size #create empty hash table
    collisionsTitle = 0 #help keep track of times something is already in the bucket
    for movie in movies:
        #feed the appropriate field into the hash function to get a key
        titleKey = function(movie.movie_title)
        #mod the key value by the hash table length
        titleIndex = titleKey % size

        #try to insert DataItem into hash table
        #check and see if a DataItem in there, if not insert
        if hashTitleTable[titleIndex] == None:
                hashTitleTable[titleIndex] = [movie]
        else:
            collisionsTitle += 1 #increment collision counter for title, already a title there
            hashTitleTable[titleIndex].append(movie)
    
    endTitle = time.time() #end time to record for title hash table
    titleTime = endTitle - startTitle
    #calculate the amount of unused buckets from title hash table
    wastedTitle = 0
    for bucket in hashTitleTable:
         if bucket == None: #checks for empty bucket
              wastedTitle += 1 #if the bucket is empty, then the counter for wastedTitle is incremented

    #Hash Table 2: Movie Quote as Key
    #This hash table will use the movie quote as the key
    #to store and retrieve movie records.
    startQuote = time.time() #start time to record for quote hash table
    hashQuoteTable = [None] * size
    collisionsQuote = 0 #help keep track of times something is already in the bucket
    
    for movie in movies:
        #feed the appropriate field into the hash function to get a key
        quoteKey = function(movie.quote)
        #mod the key value by the hash table length
        quoteIndex = quoteKey % size

        #try to insert DataItem into hash table
        #check and see if a DataItem in there, if not insert
        if hashQuoteTable[quoteIndex] == None:
            hashQuoteTable[quoteIndex] = [movie]
        else:
            collisionsQuote += 1 #increment collision counter for quote, already a quote there
            hashQuoteTable[quoteIndex].append(movie)

    endQuote = time.time() #end time to record for quote hash table
    quoteTime = endQuote - startQuote
    #calculate the amount of unused buckets from title hash table
    wastedQuote = 0
    for bucket in hashQuoteTable:
         if bucket == None: #checks for empty bucket
              wastedQuote += 1 #if the bucket is empty, then the counter for wastedQuote is incremented

    return {
        "titleTime": titleTime,
        "quoteTime": quoteTime,
        "collisionsTitle": collisionsTitle,
        "collisionsQuote": collisionsQuote,
        "wastedTitle": wastedTitle,
        "wastedQuote": wastedQuote
    }

def hashStatistics(attemptName, stats):
    titleTime = stats["titleTime"]
    quoteTime = stats["quoteTime"]
    collisionsTitle = stats["collisionsTitle"]
    collisionsQuote = stats["collisionsQuote"]
    wastedTitle = stats["wastedTitle"]
    wastedQuote = stats["wastedQuote"]

    #Optimization statistics for Title Hash Table
    print("Hash Table: Movie Title")
    print(f"Optimization Attempt:", attemptName)
    #amount of wasted space (unused buckets or slots)
    print("Amount of Wasted Space:", wastedTitle)
    #number of collisions that occurred during construction
    print("Number of Collisions:", collisionsTitle)
    #time taken to construct the hash table
    print(f"Time Taken: {titleTime:0.6f} seconds")

    print()
    print("=" * 50)

    #Optimization statistics for Quote Hash Table
    print("\nHash Table: Movie Quote")
    print(f"Optimization Attempt:", attemptName)
    #amount of wasted space (unused buckets or slots)
    print("Amount of Wasted Space:", wastedQuote)
    #number of collisions that occurred during construction
    print("Number of Collisions:", collisionsQuote)
    #time taken to construct the hash table
    print(f"Time Taken: {quoteTime:0.6f} seconds")

    print()
    print("=" * 50)

def main():
    attempts = [
        ("Simple Sum Hash Table", hashFunction),
        ("Polynomial Rolling Hash Table", hashPolynomialRolling)
    ]

    for attemptName, function in attempts:
        stats = buildHashTables(function)
        hashStatistics(attemptName, stats)


if __name__ == "__main__":
    main()
