#!/bin/bash
set -e

DB_HOST="db"
DB_PORT="5432"

echo "📦 Waiting for PostgreSQL..."
until nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 1
done
echo "✅ PostgreSQL is up."

echo "🛠️ Applying migrations..."
python manage.py migrate

echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Optional: create superuser if it doesn't exist
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  echo "👤 Creating superuser..."
  python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser(
        '$DJANGO_SUPERUSER_USERNAME',
        '$DJANGO_SUPERUSER_EMAIL',
        '$DJANGO_SUPERUSER_PASSWORD'
    )
END
fi

echo "🚀 Starting server..."
exec "$@"
