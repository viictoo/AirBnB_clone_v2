$filepath = '/etc/nginx/sites-available/hbnb_static'
$search_str = '/^\tlocation \/ {'
$err = "\terror_page 404 /404.html;\n\n"


$str = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html 0-index.html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QzOaNHdBq1A;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
    }
}"

# Run apt-get update
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
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
  content => str,
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
