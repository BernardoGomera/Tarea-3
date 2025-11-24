# Entrega - Tarea 3: CRUD + Git Flow (Programación 2 - ITLA)

Nombre: Bernardo Gomera
Asignatura: Programación 3

Resumen
-------
Este proyecto es un CRUD de estudiantes implementado con Python + Flask. Hice el desarrollo por partes usando Git Flow: trabajé cada característica en su propia rama `feature/` o `hotfix/`, luego abrí PRs hacia `develop`, `qa` y `main` y los cerré/mergeé cuando correspondía.

¿Qué hice en el proyecto?
- Creé una app pequeña que permite crear, ver, editar y eliminar estudiantes.
- Implementé una base de datos SQLite sencilla con datos de ejemplo.
- Añadí templates muy simples para que la aplicación sea usable desde el navegador.

Ramas usadas (Git Flow)
- `main`: rama estable final.
- `develop` (o `dev`): integración de features para la próxima entrega.
- `qa`: rama para pruebas antes de pasar a `main`.
- Ramas de trabajo (ejemplos):
  - `feature/login-form`: trabajo del formulario de inicio (simulado en este CRUD).
  - `feature/validate-user-input`: validación de campos en formularios.
  - `feature/payment-api-integration`: integración simulada (no usada en el CRUD final, pero creada para la tarea).
  - `feature/user-dashboard`: cambios para tablero de usuario.
  - `hotfix/fix-date-format`: arreglo rápido de formato (simulado).

Pull Requests creados
- Por cada rama de trabajo creé 3 PRs: uno hacia `develop`, otro hacia `qa` y otro hacia `main`.
- Los mensajes de los PRs y commits están escritos de forma natural, por ejemplo:
  - "Agregué la validación de correo para evitar errores cuando el usuario escribe mal."
  - "Arreglé un fallo donde el formato de fecha salía incorrecto."

Cómo terminé el merge en `main`
- Primero integré las ramas en `develop` y revisé localmente.
- Luego abrí PRs hacia `qa`, probé la app en entorno de pruebas.
- Finalmente, cuando todo estaba bien, abrí PRs hacia `main` y los mergeé para dejar la rama principal lista.

Instrucciones para replicar el proceso (resumen)
1. Clonar el repo y moverte al directorio del proyecto.
2. Ejecutar `bash gitflow_setup.sh` para crear ramas locales y commits básicos.
3. Hacer push al remoto y ejecutar `bash create_prs.sh origin` para crear PRs usando `gh`.
   - tener pendiente de haber hecho `gh auth login`
4. Para correr la app local:

```bash
cd crud
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```


