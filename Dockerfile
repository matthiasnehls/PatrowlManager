FROM python:3.7-slim
MAINTAINER cyberscan.io "matthias.nehls@dgc.org"
LABEL Name="cyberscan-frontend" Version="2023.01.13"

ENV PYTHONUNBUFFERED 1
ARG arg_http_proxy
ENV http_proxy $arg_http_proxy
ENV https_proxy $arg_http_proxy

RUN mkdir -p /opt/cyberscan-frontend/
WORKDIR /opt/cyberscan-frontend/

RUN apt-get update -yq  \
	&& apt-get install -yq --no-install-recommends apt-utils python3 python3-pip libmagic-dev python3-dev gcc wget \
	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./requirements.txt /root/

#RUN python --version \
#	&& pip3 install virtualenv \
#	&& virtualenv env3 \
#	&& /opt/cyberscan-frontend/env3/bin/pip3 install --no-cache-dir -r /root/requirements.txt

RUN python --version \
	&& pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org --default-timeout=100 virtualenv \
	&& virtualenv env3 \
	&& /opt/cyberscan-frontend/env3/bin/pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org --default-timeout=100 --no-cache-dir -r /root/requirements.txt

COPY . /opt/cyberscan-frontend/
COPY app/settings.py.sample /opt/cyberscan-frontend/app/settings.py
COPY app/assets_detection_rules.py.sample /opt/cyberscan-frontend/app/assets_detection_rules.py

EXPOSE 8003
ENTRYPOINT ["/opt/cyberscan-frontend/docker-entrypoint.sh"]
CMD ["run"]
