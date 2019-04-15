#!/bin/sh
fileid="1QBZh4aZOhJdxH3rGgaf0JdlwyTJQd2YE"
filename="fk.pth"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
mkdir models
mv fk.pth ./models/
