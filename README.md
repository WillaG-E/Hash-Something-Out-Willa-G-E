# Hash-Something-Out-Willa-G-E
Homework #5: Hash Something Out
-Analyze the statistics you collected for each approach

Optimization Attempt 1: Simple Sum Hash
This method was the first attempt function so it served as a baseline to compare the rest of attempts to. This wasn't an effective method if you are worried about the number of collisions, since they were the highest in this method. Since any strings that had a similar set of characters no matter their order caused frequent collisions. 
    
    Hash Table: Movie Title
      Amount of Wasted Space: 12249
      Number of Collisions: 11248
      Time Taken: 0.036619 seconds
    Hash Table: Movie Quote
      Amount of Wasted Space: 13277
      Number of Collisions: 12276
      Time Taken: 0.030605 seconds

While in this attempt the time taken wasn't an issue and the hash tables were compiled fast, the number of collisions and the amount of wasted space is very high. And it seems that the hash table for movie quotes had more of a problem with wasted space and collisions.


Optimization Attempt 2: Polynomial Rolling
This method using an algorithm with a polynomial base number and large prime modulus performed significantly better than in attempt 1. There was a noticeable reduction in both wasted space and collisions after the first attempt but with that the speed was slowed down.

    Hash Table: Movie Title
      Amount of Wasted Space: 7916
      Number of Collisions: 6915
      Time Taken: 0.065353 seconds
    Hash Table: Movie Quote
      Amount of Wasted Space: 6359
      Number of Collisions: 5358
      Time Taken: 0.101716 seconds

In this attempt, the amount of wasted space and number of collisions were decrased by about half. But with this improvement, the amount of time it took was doubled for the movie title hash table and the movie quote hash table's time was more than tripled.


Optimization Attempt 3: Multiplicative

    Hash Table: Movie Title
      Amount of Wasted Space: 7815
      Number of Collisions: 6814
      Time Taken: 0.038601 seconds
    Hash Table: Movie Quote
      Amount of Wasted Space: 6333
      Number of Collisions: 5332
      Time Taken: 0.479258 seconds
      
Optimization Attempt 4: DJB2

    Hash Table: Movie Title
      Amount of Wasted Space: 7951
      Number of Collisions: 6950
      Time Taken: 0.036619 seconds
    Hash Table: Movie Quote
      Amount of Wasted Space: 6302
      Number of Collisions: 5301
      Time Taken: 0.481149 seconds
      
Optimization Attempt 5: FNV-1a

    Hash Table: Movie Title
      Amount of Wasted Space: 7874
      Number of Collisions: 6873
      Time Taken: 0.052271 seconds
    Hash Table: Movie Quote
      Amount of Wasted Space: 6342
      Number of Collisions: 5341
      Time Taken: 0.079499 seconds

      
Conclusions
-Compare the performance of your different hash function approaches
-Discuss which methods were most effective and why

