# Create folders
New-Item -ItemType Directory -Force -Path src\clients
New-Item -ItemType Directory -Force -Path src\config
New-Item -ItemType Directory -Force -Path src\exceptions
New-Item -ItemType Directory -Force -Path src\models
New-Item -ItemType Directory -Force -Path src\notifications
New-Item -ItemType Directory -Force -Path src\services
New-Item -ItemType Directory -Force -Path src\storage
New-Item -ItemType Directory -Force -Path src\utils

New-Item -ItemType Directory -Force -Path tests
New-Item -ItemType Directory -Force -Path docs

# Create root files
New-Item -ItemType File -Force -Path README.md
New-Item -ItemType File -Force -Path .gitignore
New-Item -ItemType File -Force -Path .env

# Create source files
New-Item -ItemType File -Force -Path src\main.py

New-Item -ItemType File -Force -Path src\config\__init__.py
New-Item -ItemType File -Force -Path src\clients\__init__.py
New-Item -ItemType File -Force -Path src\exceptions\__init__.py
New-Item -ItemType File -Force -Path src\models\__init__.py
New-Item -ItemType File -Force -Path src\notifications\__init__.py
New-Item -ItemType File -Force -Path src\services\__init__.py
New-Item -ItemType File -Force -Path src\storage\__init__.py
New-Item -ItemType File -Force -Path src\utils\__init__.py

New-Item -ItemType File -Force -Path tests\__init__.py

Write-Host "Project structure created successfully!"