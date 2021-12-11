# set base image of host
FROM python:3.8


# sets the working directory in the container
WORKDIR /Code

#Copy files
COPY core.py core.py
COPY requirements.txt requirements.txt
COPY run.py run.py

# install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]

# command to run on container start
CMD [ "python", "./run.py"]