import subprocess


def docker_up():
    cmd = "docker compose -f infra/compose.yaml up -d".split(" ")
    subprocess.run(cmd)


def docker_stop():
    cmd = "docker compose -f infra/compose.yaml stop".split(" ")
    subprocess.run(cmd)


def docker_down():
    cmd = "docker compose -f infra/compose.yaml down".split(" ")
    subprocess.run(cmd)


def app():
    cmd = "poetry run python python_api_rds_postgres/app.py".split(" ")
    subprocess.run(cmd)
