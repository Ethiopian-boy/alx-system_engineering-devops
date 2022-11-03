# Web stack debugging #3

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

* Install puppet-lint
$ ` apt-get install -y ruby `
$ ` gem install puppet-lint -v 2.1.1 `

* 0. Strace is your friend
* Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

* Hint:

* strace can attach to a current running process
* You can use tmux to run strace in one window and curl in another one

* Requirements:

* Your 0-strace_is_your_friend.pp file must contain Puppet code
* You can use whatever Puppet resource type you want for you fix

* USAGE 
` puppet apply 0-strace_is_your_friend.pp `
