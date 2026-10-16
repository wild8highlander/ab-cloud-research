# AB-Cloud unified package — reproducible runner image
FROM python:3.12-slim

WORKDIR /pkg
COPY . /pkg

RUN pip install --no-cache-dir pyyaml typer rich

# the honesty gate at build time
RUN python3 06_code/python/run.py validate

ENTRYPOINT ["python3", "06_code/python/run.py"]
CMD ["--lang=en", "analyze"]
