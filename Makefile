build-push/multiarch:
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --tag murilokakazu/sauroniiot-classification-api:latest .

run/prod:
	PROD=True MODEL_PATH=./model/weights/model.h5 uvicorn app:app --port 8000 --reload