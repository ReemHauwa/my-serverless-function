# GCP Serverless Function

Simple HTTP-triggered serverless function deployed on Google Cloud Platform.

## Setup
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Set up GCP project
4. Deploy function: `gcloud functions deploy...`

## Local Development
```bash
python -m functions_framework --target process_input --port 8080