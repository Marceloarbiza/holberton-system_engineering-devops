# change SSH configuration file


file_line {'/etc/ssh/ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#\s{3,}PasswordAuthentication',
}

file_line {'/etc/ssh/ssh_config22':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#\s{3,}IdentityFile ~/.ssh/id_ed25519',
}
