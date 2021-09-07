build-push/multiarch:
	docker buildx build --push --platform linux/arm64/v8,linux/amd64 --tag murilokakazu/sauroniiot-classification-api:latest .