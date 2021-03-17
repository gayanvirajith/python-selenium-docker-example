APP_NAME="python3-selenium"
docker build -f Dockerfile -t "${APP_NAME}" .
docker run --rm -e APP_ENTRY_POINT="main.py" "${APP_NAME}"
