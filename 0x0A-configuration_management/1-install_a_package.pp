# Install puppet-lint using puppet:

exec { 'puppet-lint -v 2.5.0':
  command => 'gem install puppet-lint -v 2.5.0',
}
