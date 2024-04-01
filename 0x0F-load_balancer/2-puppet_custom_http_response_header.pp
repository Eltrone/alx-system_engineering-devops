nifeste Puppet pour la configuration de Nginx avec un en-tête HTTP personnalisé

# Met à jour la liste des paquets
exec { 'update_package_lists':
  command => '/usr/bin/apt-get update',
  unless  => '/usr/bin/apt-get -qq update | /bin/grep -q "All packages are up to date"',
}

# Assure que le paquet Nginx est installé
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update_package_lists'],
}

# Définit un en-tête HTTP personnalisé dans un fichier séparé
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => 'file',
  content => "add_header X-Served-By ${::hostname};",
  notify  => Service['nginx'],
}

# Gère le service Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/etc/nginx/conf.d/custom_headers.conf'],
}
