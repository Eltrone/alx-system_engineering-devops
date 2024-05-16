# Increase system file descriptor limits for high performance web services
exec { 'increase-nofile-limit-for-users':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['increase-nofile-limit-for-root'],
}

# Adjust root user file descriptor limit to ensure stability under high load
exec { 'increase-nofile-limit-for-root':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}

