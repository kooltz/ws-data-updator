# ws-data-updator
웹소켓을 통해 수신된 데이터를 자동으로 DB에 저장 


## Requirements

* python 3.9.1
* pyenv 2.0.5

## Configurations

### pyenv
```
pyenv install 3.9.1

pyenv local 3.9.1
```

### venv
```
python -m venv venv

source venv/bin/activate
```

### pip
```
pip install -m requirements.txt
```

### config.json.exmaple

`config.json.exmaple`파일을 `config.json` 파일로 복사한다.

`config.json` 파일을 열어 원하는 설정에 맞게 수정하여 사용한다.
```
{
    "WS":[
        "ID": "" # 웹소켓 연결 식별을 위한 ID
        "URL": "" # 웹소켓 서버 URL
        "PAYLOAD": { # 웹소켓 연결을 위한 payload
            ...
        }  
    ],
    "DB":{
        "URL": "" # DB URL
        "DATABASE": "" # 저장할 데이터베이스
    }
}
```

## Run

```
python main.py
```
