Just another test issue
============================================

Use the following command to build and start the project

::

    docker-compose up -d


Usage
============================================

Get help

::

    docker exec -i ucti ./get_final_url.py --help


Redirection depth can be configured
with --depth parameter, by default it equals to 2.

::

    docker exec -i ucti ./get_final_url.py http://localhost:8000/inf/ --depth 2

There is some urls to check functionality:

- http://localhost/ No redirects case
- http://localhost/1/ Case with single redire ct only
- http://localhost/{redirect_count}/ Multiple redirects
- http://localhost/inf/ Infinite redirects


Testing
============================================

::

    docker exec -i ucti pytest
