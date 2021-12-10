# set base image of host
FROM python:3.8

# sets the working directory in the container
WORKDIR /Code

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./io.py" ]