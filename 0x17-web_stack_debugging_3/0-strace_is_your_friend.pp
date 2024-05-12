# Fix Apache error 500 for WordPress on LAMP

exec { 'replace_php_string':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  unless  => 'grep -q "php" /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
}

