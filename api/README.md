# Fico alebo Kiska Web App

[![Build Status](https://travis-ci.org/QuarKUS7/fico-vs-kiska.svg?branch=master)](https://travis-ci.org/QuarKUS7/fico-vs-kiska)

Simple flask app using Resnet34 network for distinguish between image of former slovak prime minister R. Fico and slovak president A. Kiska hosted on Heroku.

## Description

I have scrapped photos of R.Fico and A.Kiska and trained pretrained Resnet34 using these images. The training was done using Fastai library. The app and it's dependencies were optimized to fit into Heroku Free Dyno.

Deployment is done using Travis-CI automaticaly into Heroku and Docker hub.

## Getting Started

Visit the [page](https://fico-alebo-kiska.herokuapp.com/)

For running locally run:
```
docker run -p 5000:5000 quarkus7/fico-vs-kiska python app.py
```
and in your browser open:
```
http://localhost:5000/
```

### Dependencies

Dependencies are listed in Dockerfile and requirements.txt

## Authors

Peter Pagac

## License

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
