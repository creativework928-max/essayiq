# Deployment

## Local
Run FastAPI with Uvicorn and the React/Vite development server.

## Container
`docker compose up --build` starts the API. Mount a trained model into `models/` or build it during a controlled training workflow.

## Production
Deploy the frontend to static hosting and the FastAPI service to a container-capable platform. Configure CORS to the actual frontend origin, use HTTPS, keep credentials outside source control, and provision model artifacts through a controlled release process.
