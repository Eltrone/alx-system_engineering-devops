# Add stable version of Nginx
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable -y',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Update software packages list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Allow HTTP traffic
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# Change folder permissions
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Create index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Create 404 page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Add redirection and error page to the Nginx default config file
file { 'Nginx default config file':
  path    => '/etc/nginx/sites-enabled/default',
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / {
        try_files \$uri \$uri/ =404;
    }
    location /redirect_me {
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => 'running',
  enable => 'true',
  require => Package['nginx'],
}
