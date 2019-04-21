FROM nginx:latest

COPY ./nginx /etc/nginx/conf.d

CMD sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d && nginx -g 'daemon off;'