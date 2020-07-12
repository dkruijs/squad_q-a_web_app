FROM nginx:1.13.7-alpine

# Overwrite nginx config
COPY ./src/app/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./src/app/website /usr/share/nginx/html

EXPOSE 80
