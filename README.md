# What is cyclop?
`cyclop` is a full python implemented bot with the aim of identify tweets of interest in the Twitter stream, like and 
retweet them. The tweets of interest are selected using a list of keywords given by you.

# How to use it?
To run `cyclop` you need three steps detailed in below sections:
1. Creating a Twitter developer account.
2. Give the keywords used to identify tweets of interest.
3. Run the bot. We recommends to use the docker container version of this bot which will let you run it with only two 
command lines. 

### Create Twitter API Authentication Credentials
You need to apply for a developer account. To apply, go to [Twitter developer site](https://developer.twitter.com/en) after 
creating a Twitter user account.

A developer account will provide the following credentials to connect to Twitter API:
- Consumer key
- Consumer secret
- Access token
- Access secret

These credentials need to be set as environment variables on the machine running the bot. 
These environment variables need to be named as follow:
- `TWITTER_CONSUMER_KEY`
- `TWITTER_CONSUMER_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`

### Keywords entry
You have to give keywords in the `cli-args.txt` a the root of the project. These keywords will be 
gotten by the project command line interface.

### Run the bot
In the project's root directory:
1. Build the docker container which will embed the bot program `docker build . -t cyclop`
2. Run the built container
```
docker run -it -e TWITTER_CONSUMER_KEY=${TWITTER_CONSUMER_KEY} \
 -e TWITTER_CONSUMER_SECRET=${TWITTER_CONSUMER_SECRET} \
 -e TWITTER_ACCESS_TOKEN=${TWITTER_ACCESS_TOKEN} \
 -e TWITTER_ACCESS_TOKEN_SECRET=${TWITTER_ACCESS_TOKEN_SECRET} \
 cyclop
```

##### Remark:
You can run this bot using the given `Makefile`:
1. Build the container `make build-cyclop`
2. Run the built container `run-cyclop`

