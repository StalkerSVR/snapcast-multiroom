cd /root/snapcastr/
#PYTHONPATH=. python ./bin/snapcastrd --bind=0.0.0.0 --port=5011 --host=$SNAPCAST_HOST
poetry run snapcastrd --sc_host=$SNAPCAST_HOST --port 5011 --host 0.0.0.0
