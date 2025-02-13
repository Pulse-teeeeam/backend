FROM python:3.10-slim as main_from

RUN mkdir app
RUN apt-get update && apt-get install -y curl && apt-get clean
WORKDIR app

ADD ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app/

RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD python manage.py migrate \
    && gunicorn -w 5 pulse_backend.wsgi:application -b 0.0.0.0:8000 --timeout 180

FROM nginx:1.23.3 as nginx_run
COPY --from=main_from /app/static /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]