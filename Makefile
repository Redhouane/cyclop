build-red-bot:
	docker build . -t red-bot

run-red-bot:
	docker run -it -e TWITTER_CONSUMER_KEY=${TWITTER_CONSUMER_KEY} \
 -e TWITTER_CONSUMER_SECRET=${TWITTER_CONSUMER_SECRET} \
 -e TWITTER_ACCESS_TOKEN=${TWITTER_ACCESS_TOKEN} \
 -e TWITTER_ACCESS_TOKEN_SECRET=${TWITTER_ACCESS_TOKEN_SECRET} \
 red-bot

bash-red-bot:
	docker exec -it gamaken bash

reset-stack:
	docker system prune --all --volumes
