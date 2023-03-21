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
## API仕様
POST:http://localhost:9000/api/detect/
・リクエスト
```
[
    {
        "id": 1,
        "spots_url": "https://www.youtube.com/watch?v=3kPH7kTphnE"
    },
    {
        "id": 2,
        "spots_url": "https://www.youtube.com/watch?v=9plqYTT-3w8"
    }
]
```
・レスポンス
```
[
    {
        "id": 1,
        "count": 5
    },
    {
        "id": 2,
        "count": 8
    }
]
```
