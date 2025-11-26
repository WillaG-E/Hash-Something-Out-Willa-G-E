# Hash-Something-Out-Willa-G-E
Homework #5: Hash Something Out

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

This method used multiplicative hashing approach that combined characters and then applied Knuth's multiplicative constant to spread values across the hash tables. The movie title hash table performed slightly better than the polynomial rolling method for collisions and wasted space. But, the movie quote hash table, wasted space and collisions were reduced compared to the previous two attempts, the time taken was increased significantly.

    Hash Table: Movie Title
      Amount of Wasted Space: 7815
      Number of Collisions: 6814
      Time Taken: 0.038601 seconds
    Hash Table: Movie Quote
      Amount of Wasted Space: 6333
      Number of Collisions: 5332
      Time Taken: 0.479258 

In this attempt, both wasted space and collisions were improved compared to the polynomial rolling hash function. The movie title hash table was almost created as quickly as the simple sum hash table attempt. But the movie quote hash table took the longest out of the attempts up to this point.
      
Optimization Attempt 4: DJB2

This method used a DJB2 hashing algorithm that repeatedly multiplied the current hash key by 33 and then added the character code. The movie title hash table for this attempt was very similar to the Polynomial Rolling method. The values of wasted space and collisions were very similar but it took less time to construct. For the movie quote hash table this method was able to achieve the lowest wasted space and the fewest collisions, but the time taken was sacrificed.

    Hash Table: Movie Title
      Amount of Wasted Space: 7951
      Number of Collisions: 6950
      Time Taken: 0.036619 seconds
    Hash Table: Movie Quote
      Amount of Wasted Space: 6302
      Number of Collisions: 5301
      Time Taken: 0.481149 seconds

In this attempt, the title hash table stayed efficient and was very quick to build in a similar time as the simple sum function, but with a big decrease in collisions. The quote hash table for the DJB2 method had the least amount of wasted space and a low collision count, but these improvements came with it being the slowest construction time for the quote hash tables.
      
Optimization Attempt 5: FNV-1a

This method uses the FNV-1a hashing algorithm. This method combines XOR operations using multiplication of a large prime number and keeps the hash value within 32 bits.

    Hash Table: Movie Title
      Amount of Wasted Space: 7874
      Number of Collisions: 6873
      Time Taken: 0.052271 seconds
    Hash Table: Movie Quote
      Amount of Wasted Space: 6342
      Number of Collisions: 5341
      Time Taken: 0.079499 seconds

In this attempt, FNV-1a provided a consistently strong performance. This method kept collisions and wasted space low for both the title and quote hash tables, while not sacrificing the time taken. This had one of the best balances between the time taken and keeping the number of collisions and wasted space lower.

      
Conclusions

All of the different hash function approaches ran fairly similar, except for Optimization Attempt 1. 

        Rankings by Amount of Wasted Space (Title)
            Multiplicative: 7815
            FNV1-a: 7874
            Polynomial Rolling: 7916
            DJB2: 7951
            Simple Sum: 12249

        Rankings by Amount of Wasted Space (Quote)
            DJB2: 6302
            Multiplicative: 6333
            FNV-1a: 6342
            Polynomial Rolling: 6359
            Simple Sum: 13277

        Rankings by Number of Collisions (Title)
            Multiplicative: 6814
            FNV-1a: 6873
            Polynomial Rolling: 6915
            DJB2: 6950
            Simple Sum: 11248

        Rankings by Number of Collisions (Quote)
            DJB2: 5301
            Multiplicative: 5332
            FNV-1a: 5341
            Polynomial Rolling: 5358
            Simple Sum: 12276

        Rankings by Time Taken (Title)
            Simple Sum: 0.036619 seconds
            DJB2: 0.036619 seconds
            Multiplicative: 0.038601 seconds
            FNV-1a: 0.052271 seconds
            Polynomial Rolling: 0.065353 seconds

        Rankings by Time Taken (Quote)
            Simple Sum: 0.030605 seconds
            FNV-1a: 0.079499 seconds
            Polynomial Rolling: 0.101716 seconds
            Multiplicative: 0.479258 seconds
            DJB2: 0.481149 seconds
            
Overall, the Simple Sum hash function was the least effective out of all five optimization attempts. Even though the Simple Sum was the fastest for both the title and movie quote hash tables, it produced the highest amount of collisions and the most wasted space. This occurrs since the Simple Sum hash function only adds the character codes so strings with similar characters but in different orders cause collisions. 
Since the polynomial rolling hash function uses character order and a large prime modulus that helps to spread values. The Polynomial Rilling function is significantly slower, especially when the strings or quotes are long causing more time. 
The Multiplicative hash function is also a polynomial-style hash but it is capped to avoid huge values. For titles, this hash function gave the fewest collisions and the least amount of wasted space. The Multiplicative hash function is the most consistent, and the best to compile titles. While quotes are longer strings so they require more loop work. 
The DJB2 hash function performed the best for collisions and wasted space for the quote hash table. But it also had the slowest time taken for quotes at roughly 0.48 seconds. This slowness probably is caused by the longer strings needing more iterations.
In conclusion, the best overall are FNV-1a, Multiplicative, and DJB2. But if you wanted to pick a hash function that creates the best balanced hash table it would probably be FNV-1a due to its fewer collisions and avoids worse performance that some of the other hash functions showed on the quote hash table.
