FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc curl

WORKDIR /app

#RUN apk --no-cache --update-cache add make g++ gfortran libgfortran python-dev libstdc++ subversion
#py-pip build-base freetype-dev libpng-dev openblas-dev \
#    && rm -rf /var/cache/apk/*

RUN pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cpu/torch_nightly.html
RUN pip install scipy
RUN pip install fastai==1.0.34

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN ./model_download.sh

CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
