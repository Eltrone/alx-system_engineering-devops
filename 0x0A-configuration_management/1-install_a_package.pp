# This manifest ensures the flask package is installed via pip3 at version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
