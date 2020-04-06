FROM python:3.7-slim

WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -Ur requirements.txt && \
    chmod +x /app/entrypoint.sh && \
    chmod +x /app/manage.py && \
    chmod +x /app/get_final_url.py
ENTRYPOINT ["/app/entrypoint.sh"]
