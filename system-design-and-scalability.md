*Source Text*: McDowell, G. L. (2015). Chapter 9: System Design & Scalability in Cracking the Coding Interview in 189 Programming Questions and Solutions. CareerCup.

# Tips:
* communicate
* go broad first
* use the whiteboard
* acknowledge interviewer concerns
* be careful about assumptions
* state your assumptions explicitly
* estimate when necessary
* drive

# Design: Step-By-Step
* scope the problem
* make reasonable assumptions
* draw the major components
* identify the key issues
* redesign for the key issues

# Algorithms That Scale Step-By-Step
* ask questions
* make believe (pretend all the data can fit etc etc idealize)
* get real
* solve problems

# KEY CONCEPTS
* Horizontal vs Vertical Scaling
* Load Balancer
    * throw frontend of website to a load balancer
* Database Denormalization and NoSQL
* Database Partitioning
    * vertical partitioning
        * partitioning by feature
    * key-based or hash-based partitioning
    * directory-based partitioning
* Caching
    * in-memory cache = simple key-value pairing and sits between your application layer & data store
        * cache query directly/cache object
* Asynchronous processing & queues
* Networking Metrics
      * bandwith
      * thoroughput
      * latency
  * Conveyor Belt Example:
      * fatter conveyor belt --> improve thoroughput and bandwith but not latency
      * shorten belt --> improve latency
      * faster conveyor belt --> improve all three
* MapReduce

# Considerations
* failures
* availability & reliability
* read-heavy vs write-heavy
* security

# There is no perfect system

# Example Problem: How would you find all documents that contain a list of words?
* step 1: simple case of a few dozen
* step 2: what happens when we increase docs? multiple machines? qs:
    * how do we divide our hash table?
    * do we need to process documents on one machine & then push off to another machine? if so, how?
    * lookup table for which machine holds which piece of data
* step 3: solutions
    * divide the words alphabetically and store on machine until space complete (disadvantage = reinsertion)
    

    
