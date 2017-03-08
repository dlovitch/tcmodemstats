tcmodemstats
============

tcmodemstats is a Technicolor Cable Modem Statistics Scraper and Forwarder. It currently supports forwarding stats to Datadog (via the API).

Components
----------
There are currently two ways to use tcmodemstats:

cli.py
~~~~~~
Running ``cli.py`` is a command line program which requires arguments passed in and returns statistics information as pretty-printed JSON.

An example for running this would be ``/cli.py -h 192.168.0.1 -u admin -p password`` (assuming ``192.168.0.1`` is the cable modem IP and the login information is ``admin``/``password``).

modemstatsforwarder.py
~~~~~~~~~~~~~~~~~~~~~~
In order to have stats continually retrieved and forwarded to a datastore, ``modemstatsforwarder.py`` is designed to require minimal command line input and to keep configuration parameters in either a configuration file or environment variables. After configuration, simply run ``./modemstatsforwarder.py``.

Forwarder Configuration
-----------------------

The following is a list of configuration variables and example values needing to be defined. These can either be set via environment variables or a configuration file.

::

    tcmodem_name=yourcablemodem
    tcmodem_username=admin
    tcmodem_password=password
    tcmodem_host=192.168.0.1
    stats_destination=datadog
    datadog_endpoint=https://app.datadoghq.com/api/
    datadog_api_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    datadog_app_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

``tcmodem_name``
~~~~~~~~~~~~~~~~
A name for the modem. Can be any string.

``tcmodem_username`` and ``tcmodem_password``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The login information to the web interface of the modem.

``tcmodem_host``
~~~~~~~~~~~~~~~~
The IP address or hostname of the cable modem's web interface.


``stats_destination``
~~~~~~~~~~~~~~~~~~~~~
This parameter currently only supports one option, ``datadog``.

``datadog_endpoint``
~~~~~~~~~~~~~~~~~~~~
The URL for the Datadog API (should likely always be ``https://app.datadoghq.com/api/``).

``datadog_api_key`` and ``datadog_app_key``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create or retrieve these values from https://app.datadoghq.com/account/settings#api
