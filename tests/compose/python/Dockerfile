# Base image
FROM debian:stable

# Copy data to container
COPY dev_requirements_3.txt /tmp/dev_requirements_3.txt
COPY dev_requirements_2.txt /tmp/dev_requirements_2.txt

# Copy scripts to container
COPY ./tests/compose/python/init.sh /tmp/init.sh
COPY ./tests/scripts/filter-python-versions.py /tmp/filter-python-versions.py
COPY ./tests/scripts/pyenv-install.sh /tmp/pyenv-install.sh

# Run container init script
RUN chmod +x /tmp/init.sh
RUN bash -c "/tmp/init.sh |& tee -a /root/init.log"

# Run pyenv install
RUN chmod +x /tmp/pyenv-install.sh
RUN bash -c "/tmp/pyenv-install.sh |& tee -a /root/pyenv_install.log"
