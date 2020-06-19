{% for user in pillar['users'] %}
add_{{ user }}:
  user.present:
    - name: {{ user }}
{% endfor %}

{% if 'my_ssh_key' in pillar %}
manage_my_ssh_key:
  file.managed:
    - name: /root/.ssh/{{ pillar['my_ssh_key_name'] }}
    - mode: 600
    - contents_pillar: my_ssh_key
    - show_diff: False
{% endif %}
