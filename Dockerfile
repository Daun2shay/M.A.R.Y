# set base image of host
FROM python:3.8


# sets the working directory in the container
WORKDIR /Code

#Copy files
COPY IO.py code.py
COPY requirements.txt requirements.txt
COPY 

# install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]

# command to run on container start
CMD [ "python", "./code.py"]