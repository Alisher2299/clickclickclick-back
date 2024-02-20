#!/bin/bash

wait_for () {
    for _ in seq 0 100; do
        (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
        if [[ $? -eq 0 ]]; then
            echo "$1:$2 accepts connections!^_^"
            break
        fi
        sleep 1
    done
}

populate_env_variables () {
  set -o allexport
  [[ -f /src/core/.env ]] && source /src/core/.env
  set +o allexport
  echo "env variables are populated!^_^"
}

populate_env_variables

case "$PROCESS" in
"DJANGO")
    wait_for "${DB_HOST}" "${DB_PORT}"

    if [[ "$LOCAL" == "True" ]]; then
        echo "🚜🚜🚜 LOCAL RUN"
        python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
    else
        echo "🏎🏎🏎 We in the rocket"
        python manage.py collectstatic --noinput && python manage.py migrate
        gunicorn -c core/gunicorn.py core.wsgi
    fi
    ;;
"DEV_CELERY")
    wait_for "${DB_HOST}" "${DB_PORT}"
    celery -A core worker -B --loglevel=INFO --concurrency=1
    ;;
"TEST")
    wait_for "${DB_HOST}" "${DB_PORT}"
    pytest -v --cov . --cov-report term-missing --cov-fail-under=10 \
    --color=yes -n 4 --no-migrations --reuse-db -W error \
    -W ignore::ResourceWarning -W ignore::DeprecationWarning \
    -W ignore::UserWarning -W ignore::RuntimeWarning
    ;;
"CELERY_SCHEDULER")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core beat --loglevel=INFO
    ;;
"CELERY_CONSUMER")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    python manage.py collectstatic --noinput
    celery -A core worker --loglevel=INFO \
    --concurrency=12 --max-tasks-per-child=2048
    ;;
*)
    echo "NO PROCESS SPECIFIED!>_<"
    exit 1
    ;;
esac