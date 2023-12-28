# Docker commands

1. docker build -t spellingbee-solution -f dockerfile .
2. docker run -p 8000:8000 spellingbee-solution
3. docker run --rm -it --name beeshell -p 8000:8000 spellingbee-solution /bin/sh

## Pushing to ECR

1. aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 561095088313.dkr.ecr.eu-central-1.amazonaws.com
2. docker tag spellingbee-solution 561095088313.dkr.ecr.eu-central-1.amazonaws.com/spellingbee-solution
3. docker push 561095088313.dkr.ecr.eu-central-1.amazonaws.com/spellingbee-solution
