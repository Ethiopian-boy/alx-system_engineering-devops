# fix nginx server client requests to get no errors
exec { 'modify limit':
  command  => "sed -i 's/15/30000/g' /etc/default/nginx; sudo service nginx reload; sudo service nginx restart",
  provider => shell,
}
