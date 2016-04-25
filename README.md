# rate_counter
Test project to count students rate based on their marks


Set up

- Create a virtual env
- activate it
- install dependencies from requirements.txt


#### Background parsing instructions (by Scandie) ####

###### On your machine: ######

  - install Redis server:
    - wget http://download.redis.io/releases/redis-3.0.7.tar.gz
    - tar xzf redis-3.0.7.tar.gz
    - cd redis-2.8.17
    - make
    - make test
    - sudo make install
    - cd utils
    - sudo ./install_server.sh
    
  - start Redis server:
    - sudo service redis_6379 start
   
###### In virtual env: #######

  - pip install -r requirements.txt
  - sudo chmod +x get-data.sh
  - ./get-data.sh
  