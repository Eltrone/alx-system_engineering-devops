# Fix Apache error 500 for WordPress on LAMP
file { '/path/to/the/problematic/file':
  ensure => 'file',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
  source => 'puppet:///modules/module_name/problematic_file',
}

exec { 'restart-apache':
  command     => '/etc/init.d/apache2 restart',
  refreshonly => true,
  subscribe   => File['/path/to/the/problematic/file'],
}
