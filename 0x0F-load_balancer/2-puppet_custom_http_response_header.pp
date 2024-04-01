# Ce manifeste Puppet configure Nginx pour ajouter un en-tête HTTP personnalisé

class nginx_custom_header {
  # Assurez-vous que le service Nginx est installé et en cours d'exécution.
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    require    => Package['nginx'],
  }

  # Définissez le nom d'hôte du serveur comme une variable.
  $hostname = $::fqdn

  # Configurez Nginx pour ajouter l'en-tête HTTP personnalisé.
  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => file,
    content => template('nginx/custom_header.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Appliquez la classe définie ci-dessus pour effectuer la configuration.
include nginx_custom_header
 mv /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.backup
sudo cat <<EOF | sudo tee /etc/haproxy/haproxy.cfg
global
    log /dev/log    local0
    log /dev/log    local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats timeout 30s
    user haproxy
    group haproxy
    daemon
    ca-base /etc/ssl/certs
    crt-base /etc/ssl/private
    ssl-default-bind-ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:RSA+AESGCM:RSA+AES:!aNULL:!MD5:!DSS
    ssl-default-bind-options no-sslv3


defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000
    errorfile 400 /etc/haproxy/errors/400.http
    errorfile 403 /etc/haproxy/errors/403.http
    errorfile 408 /etc/haproxy/errors/408.http
    errorfile 500 /etc/haproxy/errors/500.http
    errorfile 502 /etc/haproxy/errors/502.http
    errorfile 503 /etc/haproxy/errors/503.http
    errorfile 504 /etc/haproxy/errors/504.http

frontend main
    bind *:80
    mode http
    default_backend webservers

backend webservers
    balance roundrobin
    server web01 528728-web-01:80 check
    server web02 528728-web-02:80 check
EOF



# Restart HAProxy
sudo systemctl enable haproxy
sudo service haproxy restart
sudo cat <<EOF | sudo tee /etc/haproxy/haproxy.cfg
global
    log /dev/log    local0
    log /dev/log    local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats timeout 30s
    user haproxy
    group haproxy
    daemon
    ca-base /etc/ssl/certs
    crt-base /etc/ssl/private
    ssl-default-bind-ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:RSA+AESGCM:RSA+AES:!aNULL:!MD5:!DSS
    ssl-default-bind-options no-sslv3


defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000
    errorfile 400 /etc/haproxy/errors/400.http
    errorfile 403 /etc/haproxy/errors/403.http
    errorfile 408 /etc/haproxy/errors/408.http
    errorfile 500 /etc/haproxy/errors/500.http
    errorfile 502 /etc/haproxy/errors/502.http
    errorfile 503 /etc/haproxy/errors/503.http
    errorfile 504 /etc/haproxy/errors/504.http

frontend main
    bind *:80
    mode http
    default_backend webservers

backend webservers
    balance roundrobin
    server web01 528728-web-01:80 check
    server web02 528728-web-02:80 check
EOF



# Restart HAProxy
sudo systemctl enable haproxy
sudo service haproxy restart
