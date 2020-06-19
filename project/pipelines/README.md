# Build Docker image

First log into the Ali Docker registry via
```bash
sudo docker login --username=<user name>@your-appid registry.cn-beijing.aliyuncs.com
```

Build docker image under the folder `pipelines`
```bash
sh build_image.sh
```

# Bugs
- sometimes, it can't trigger the next step when seq pipelines