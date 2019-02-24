FROM python:3.6.2

# directories needed
RUN mkdir -p /home/project/app
RUN mkdir -p /home/project/app/models
WORKDIR /home/project/app

# copy and install requirements
COPY requirements.txt /home/project/app
RUN pip install --no-cache-dir -r requirements.txt

# copy content
COPY . /home/project/app
COPY ./models /home/project/app/models
