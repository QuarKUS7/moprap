FROM nginx

COPY ./nginx.conf /etc/nginx/conf.d/nginx.conf

CMD sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/nginx.conf && nginx -g 'daemon off;'