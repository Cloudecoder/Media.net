FROM httpd:2.4-alpine

COPY ./index.html /usr/local/apache2/htdocs/

COPY httpd.conf /usr/local/apache2/conf/httpd.conf

VOLUME . /usr/local/apache2

EXPOSE 80

CMD [ "httpd-foreground" ]