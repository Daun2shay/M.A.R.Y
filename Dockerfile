# set base image of host
FROM python:3.8

# sets the working directory in the container
WORKDIR /Code

COPY requirements.txt requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

# command to run on container start
CMD [ "python3", "./io.py" ]