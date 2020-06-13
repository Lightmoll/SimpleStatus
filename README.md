# SimpleStatus
 
_fast & super lightweight status server_

The server is build on Flask, it is designed to provide a minimalistic status of ones location for traveling, etc.

# Setup

## Run the Server
For testing purposes you can simply call the server with `python3 server.py`. The server listens at port 8500 and the default password is admin.
Note, that the debug mode is activated like this. __Do not use this in production__

## Run Server in Production
I ran this server in production for about half a year without any issues on a low traffic server. I recommend using ngnix and gunicorn3. During login the password is POSTed to the server as clear text, for this reason alone __HTTPS is necessary__ in a production build. I can recommend Let's Encrypt for free SSL certificates.

## Set a password
At this point you have to call the `setPassword.py` script to change the password. It will save the password as a SHA256 hash, unsalted.

# Problems
The server desperately needs a better database and preferably password salting.
