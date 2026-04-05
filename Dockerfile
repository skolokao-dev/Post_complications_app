# Используем конкретную версию Python
FROM python:3.11-slim

# Рабочая папка внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Открываем порт Streamlit
EXPOSE 8501

# Команда запуска Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]
