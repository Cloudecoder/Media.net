FROM httpd:2.4-alpine

WORKDIR /usr/local/apache2/htdocs/

COPY ./htdocs/ /usr/local/apache2/htdocs/

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

EXPOSE 80

CMD [ "httpd-foreground" ]
