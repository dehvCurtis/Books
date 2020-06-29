FROM fedora
RUN dnf install -y httpd && dnf clean all
RUN mkdir -p /var/www/html
ADD index.html /var/www/html
CMD ["/usr/bin/httpd","-DFOREGROUND"]
