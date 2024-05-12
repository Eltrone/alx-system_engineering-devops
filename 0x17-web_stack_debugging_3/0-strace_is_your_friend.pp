# Fix Apache error 500 for WordPress on LAMP

exec {'replace_php_string':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
