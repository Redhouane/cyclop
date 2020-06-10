bot-up:
	$(info "Building bot...")
	docker build . -t red-bot
	docker run -it -e TWITTER_CONSUMER_KEY=${TWITTER_CONSUMER_KEY} \
 --env TWITTER_CONSUMER_SECRET=${TWITTER_CONSUMER_SECRET} \
 --env TWITTER_ACCESS_TOKEN=${TWITTER_ACCESS_TOKEN} \
 --env TWITTER_ACCESS_TOKEN_SECRET=${TWITTER_ACCESS_TOKEN_SECRET} \
 --name bot\
 red-bot

bash-bot:
	docker exec -it red-bot bash

reset-stack:
	docker system prune --all --volumes
