$filepath = '/etc/nginx/sites-available/hbnb_static'
$search_str = '/^\tlocation \/ {'
$err = "\terror_page 404 /404.html;\n\n"

$str="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\tindex index.html 0-index.html 0-index.htm;\n\t}"


# Run apt-get update
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  user    => root,
}

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create directories
file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create and populate index.html
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "RIP ME OUT THE PLASTIC I BEEN ACTING BRAND NEW\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Add Nginx configuration
file { '/etc/nginx/sites-available/hbnb_static':
  ensure  => present,
  content => template('your_module/hbnb_static.erb'),
  notify  => Service['nginx'],
}
exec { 'Ngina Redirect Config':
  command => "sed -i '${search_str}/i \ ${redirect_me}' ${filepath}",
  path    => '/usr/bin',
  notify  => Service['nginx'],

}
exec { 'Ngina Error Page Config':
  command => "sed -i '${search_str}/i \ ${err}' ${filepath}",
  path    => '/usr/bin',
  notify  => Service['nginx'],
}
exec { 'Ngina redirect':
  command => "sudo sed -i '/^\tserver_name .*;/a ${str}' ${filepath}",
  path    => '/usr/bin',
  notify  => Service['nginx'],
}

# Enable the site
file { '/etc/nginx/sites-enabled/hbnb_static':
  ensure  => link,
  target  => '/etc/nginx/sites-available/hbnb_static',
  require => File['/etc/nginx/sites-available/hbnb_static'],
}

# Define the Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-enabled/hbnb_static'],
}
