FROM python:2.7

RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 5.11.1

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		mysql-client libmysqlclient-dev \
		postgresql-client libpq-dev \
		sqlite3 \
		locales-all \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app/tracker /usr/src/app/tracker_ui /usr/src/app/db
COPY tracker/requirements.txt /usr/src/app/tracker/
RUN (cd /usr/src/app/tracker && pip install --no-cache-dir -r requirements.txt)

COPY tracker_ui/requirements.txt /usr/src/app/tracker_ui/
COPY tracker_ui/package.json /usr/src/app/tracker_ui/
COPY tracker_ui/npm-shrinkwrap.json /usr/src/app/tracker_ui/
RUN (cd /usr/src/app/tracker_ui && pip install --no-cache-dir -r requirements.txt && npm i)

COPY django-paypal /usr/src/app/django-paypal
RUN (cd /usr/src/app/django-paypal && python setup.py install)

COPY *.py *.json /usr/src/app/
COPY tracker/ /usr/src/app/tracker/
COPY tracker_ui/ /usr/src/app/tracker_ui/

WORKDIR /usr/src/app

RUN ["python", "manage.py", "migrate"]
RUN ["python", "manage.py", "loaddata", "blank.json"]

ARG superusername=admin
ARG superuserpassword=password

RUN python manage.py createsuperuser --noinput --email nobody@example.com --username ${superusername}
RUN yes ${superuserpassword} | python manage.py changepassword ${superusername}

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8088"]
