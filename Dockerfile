FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/bmd
WORKDIR /opt/quizkingzapi
COPY requirements.txt /opt/quizkingzapi
RUN pip install -r requirements.txt
COPY . /opt/quizkingzapi/
RUN python manage.py collectstatic --no-input  # <-- here
RUN chmod ugo+x /opt/quizkingzapi/config/install/preinstall.sh
RUN /opt/quizkingzapi/config/install/preinstall.sh

# expose the port 8000
EXPOSE 8000
# define the default command to run when starting the container
CMD ["gunicorn", "--config", "/opt/quizkingzapi/config/gunicorn/gunicorn.conf.py", "bmd_backend.wsgi:application"]