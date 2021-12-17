# set base image of host
FROM python:3.8


# sets the working directory in the container
WORKDIR /Code

#Copy files
COPY core.py /Code/core.py
COPY input.py /Code/input.py
COPY run.py /Code/run.py
COPY voiceInteractions.py /Code/voiceInteractions.py
COPY logFile.txt  /Code/logFile.txt

# install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]

# command to run on container start
CMD [ "python", "./run.py"]