
#!/usr/bin/env bash

IMAGE_ID="registry.cn-beijing.aliyuncs.com/he-test/kube-pipelines:latest"
docker image build -t ${IMAGE_ID} . -f ./env/Dockerfile
docker push ${IMAGE_ID}