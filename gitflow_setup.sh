#!/usr/bin/env bash
set -e

# Script para crear ramas locales y commits realistas siguiendo Git Flow.
# USO: bash gitflow_setup.sh

ROOT=$(pwd)
echo "Iniciando setup Git Flow local..."

if [ ! -d .git ]; then
  git init
  git add -A
  git commit -m "Inicial: agregar proyecto CRUD y archivos base"
  echo "Repositorio git inicializado."
fi

# Asegurarse de que main exista
git checkout -B main

git branch -f develop || true
git checkout -B develop
git commit --allow-empty -m "Crear branch develop" || true

git checkout -B qa
git commit --allow-empty -m "Crear branch qa" || true

BRANCHES=(
  "feature/login-form"
  "feature/validate-user-input"
  "feature/payment-api-integration"
  "feature/user-dashboard"
  "hotfix/fix-date-format"
)

for b in "${BRANCHES[@]}"; do
  git checkout -B "$b" main
  FILE="features/$(echo $b | sed 's#/#-#g').txt"
  mkdir -p features
  echo "Trabajo en $b" > "$FILE"
  git add "$FILE"
  git commit -m "${b}: agregar archivo inicial para la rama" || true
done

git checkout develop
echo "Ramas creadas localmente:"
git branch --list

echo "Listo. Ahora tienes ramas feature/hotfix locales con commits realistas."
