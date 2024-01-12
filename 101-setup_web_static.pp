# script that sets up your web servers for the deployment of web_static
package {'nginx':
  ensure => 'installed'
}
exec {'create folders v1':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell
}

exec {'create folders v2':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell
}

file {'/data/web_static/releases/test/index.html':
  content => 'Hello World'
}

exec {'symbolic link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell
}

exec {'change ownership':
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  provider => shell
}

exec {'change nginx config':
  command  => 'sudo sed -i "s/root \/var\/www\/html;/\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}/" /etc/nginx/sites-available/default',
  provider => shell
}

exec {'nginx restart':
  command  => 'sudo service nginx restart',
  provider => shell
}
