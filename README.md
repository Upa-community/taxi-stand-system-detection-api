# taxi-stand-system-detection-api
タクシー乗り場の可視化・効率化システムの物体検出用API。  
## 環境構築  
1.Dockerコンテナのビルド
```
docker-compose up -d --build
```
2.コンテナに入る
```
docker container exec -it taxi-stand-system-detection-api-python-1 bash
```
3.実行
```
python batch.py
```
