# pull official base image
FROM python:3.8-alpine

# set environment varibles
ENV PYTHONUNBUFFERED 1

# create and set work directory
RUN mkdir /bots
WORKDIR /bots
COPY . /bots/

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

# Add --dev option to install dev packages
RUN pipenv install --system --deploy --ignore-pipfile

# run the bots program
CMD ["python", "bots/like_retweet.py", "@cli-args.txt"]
