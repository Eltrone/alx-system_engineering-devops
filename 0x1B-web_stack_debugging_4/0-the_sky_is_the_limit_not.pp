# Increase the maximum number of file descriptors for Nginx
exec { 'increase-file-descriptors':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/bin:/usr/bin',
}

# Restart Nginx to apply configuration changes
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
}

