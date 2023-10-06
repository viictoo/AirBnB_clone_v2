# brute force method

exec { 'command':
command  => "sudo apt-get -y update;
sudo apt-get -y install nginx;
mkdir -p /data/web_static/shared;
mkdir -p /data/web_static/releases/test/;
sudo echo 'RIP ME OUT THE PLASTIC I BEEN ACTING BRAND NEW' | sudo tee /data/web_static/releases/test/index.html;
sudo ln -nfs /data/web_static/releases/test /data/web_static/current;
sudo chown -R ubuntu:ubuntu /data;
sudo sed -i '/^\tserver_name .*;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/curre
nt/;\n\tindex index.html 0-index.html 0-index.htm;\n\t}' /etc/nginx/sites-enabled/default;;
sudo service nginx restart",
provider => shell,
}
