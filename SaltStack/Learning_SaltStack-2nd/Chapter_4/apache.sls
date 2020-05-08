install_apache:
  pkg.installed:
    - name: apache2

apache running:
  service.running:
    - name: apache2
    - enable: True
    - require:
        - pkg: install_apache