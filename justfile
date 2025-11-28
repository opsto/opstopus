restart:
    docker-compose restart opstopus
test:
    docker-compose exec opstopus pytest tests/ -v
