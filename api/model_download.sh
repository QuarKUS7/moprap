#!/bin/sh
fileid="1SCKFTEVHB-jRKXanqap6f7ErV1JXM32v"
filename="fk.pth"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
mkdir models
mv fk.pth ./models/