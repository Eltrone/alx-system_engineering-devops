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
    notify  => Service['nginx'],
  }
}

# Appliquez la classe définie ci-dessus pour effectuer la configuration.
include nginx_custom_header

