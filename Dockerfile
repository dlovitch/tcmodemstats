FROM python:3
MAINTAINER <1191170+dlovitch@users.noreply.github.com>
RUN mkdir -p /srv/app/

WORKDIR /srv/app/
COPY README.rst /srv/app/
COPY requirements.txt /srv/app/
COPY setup.py /srv/app/
COPY tcmodemstats/ /srv/app/tcmodemstats
RUN pip install --no-cache-dir .[datadog]

CMD [ "tcmodemstatsforwarder" ]
