#Author: Willa Galipeau-Eldridge
#Date: 11/18/2025
#Purpose: HW5: Hash Something Out; Hash Tables

import time
import csv
import re
from datetime import datetime

#needed: handle collision function or inserts as a linkList
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
    pass

#Create an empty Hash Table
size = 16000
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

counter = 0
collisionsTitle = 0
collisionsQuote = 0
#Load the movie data from the provided input file
file = "MOCK_DATA.csv"
start = time.time()
with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if (counter == 0):
            continue
        print(row)
        #create a DataItem from row
        movie = DataItem(row)
        #feed the appropriate field into the hash function
        #to get a key
        titleKey = hashFunction(movie.movie_title)
        quoteKey = hashFunction(movie.quote)
        #mod the key value by the hash table length

        #try to insert DataItem into hash table
        #check and see if a DataItem in there, if not insert
        if hashTitleTable[titleKey] == None:
                hashTitleTable[titleKey] = movie
        else:
             pass
        
        if hashQuoteTable[quoteKey] == None:
                hashQuoteTable[quoteKey] = movie
        else:
             pass
        hashTitleTable.append(titleKey)
        hashQuoteTable.append(quoteKey)
        #handle any collisions
        #if counter = 0; don't insert

        
    #Parse the data to extract movie titles and quotes
        counter += 1
print(counter)

#Handle any edge cases in the data (empty fields, special characters, etc.)

#Create two separate hash tables
#Hash Table 1: Movie Title as Key
#This hash table will use the movie title to store
#and retrieve movie records.

#Hash Table 2: Movie Quote as Key
#This hash table will use the movie quote as the key
#to store and retrieve movie records.


#5 optimization attempts must use fundamentally different approaches
#prime numbers are key here
    #linkedList
    #Linear probing

#track the following: #prino
    #amount of wasted space (unused buckets or slots)
    #number of collisions that occurred during construction
    #time taken to construct the hash table
end = time.time()
print(f"{end-start:0.2f} seconds")

#Submit
    #repository
    #screenshots (10 total) of results of 5 hash function variations
    #readMe --> analysis of methods
