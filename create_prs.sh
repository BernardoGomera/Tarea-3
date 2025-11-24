#!/usr/bin/env bash
set -e

# Script para crear PRs usando la CLI de GitHub (gh).
# Requisitos: tener el repo en remoto en GitHub y haber hecho 'gh auth login'.
# USO: bash create_prs.sh <remote>

REMOTE=${1:-origin}

BRANCHES=(
  "feature/login-form"
  "feature/validate-user-input"
  "feature/payment-api-integration"
  "feature/user-dashboard"
  "hotfix/fix-date-format"
)

for b in "${BRANCHES[@]}"; do
  echo "Procesando branch: $b"
  git checkout "$b"
  # Push branch
  git push -u "$REMOTE" "$b"

  # PR hacia develop
  gh pr create --base develop --head "$b" --title "${b}: PR hacia develop" --body "Agregué cambios de ${b} para integrar en develop."
  # PR hacia qa
  gh pr create --base qa --head "$b" --title "${b}: PR hacia qa" --body "Preparando pruebas en QA para ${b}."
  # PR hacia main
  gh pr create --base main --head "$b" --title "${b}: PR hacia main" --body "Merge final de ${b} a main cuando esté listo."

  # Opcionalmente, buscar PRs abiertos creados y hacer merge (se puede comentar si quieres revisar manualmente)
  # Aquí cerramos/mergeamos las PRs recién creadas para simular PRs cerrados.
  sleep 1
  PRS=$(gh pr list --head "$b" --state open --json number -q '.[].number')
  for p in $PRS; do
    echo "Mergeando PR #$p"
    gh pr merge "$p" --merge --admin || gh pr close "$p" --comment "Cerrado tras revisión." || true
  done
done

echo "Hecho. Se crearon PRs hacia develop, qa y main y se intentó mergearlos/cerrarlos."
