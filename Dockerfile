# set base image of host
FROM python:3.8

# sets the working directory in the container
WORKDIR /

#Copy files
COPY core.py /core.py
COPY input.py /input.py
COPY run.py /run.py
COPY voiceInteractions.py /voiceInteractions.py
COPY logFile.txt  /logFile.txt
COPY requirements.txt /requirements.txt

# install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]

# command to run on container start
CMD [ "python", "./run.py"]