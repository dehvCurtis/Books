# Apache web server running on Fedora Linux
FROM fedora
RUN dnf install -y httpd && dnf clean all
CMD ["/usr/sbin/httpd","DFOREGROUND"]
