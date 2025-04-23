FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV PORT 8080
EXPOSE 8080
CMD ["python", "app.py"]
