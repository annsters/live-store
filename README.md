# live-store

## setup
### server
first, setup pyenv and pyenv-virtualenv.

then:
```
pyenv virtualenv 3.7.7 store-server
pyenv activate store-server
pip install -r requirements.txt
```
### client
```
npm install
```
then, click "run in web browser" on expo cli

### db
install docker
```
docker pull postgres
mkdir -p $HOME/docker/volumes/postgres
```

## run stuff
### server
```
cd server
python server.py
```
### client
```
npm start
```
### db (should only need to do once)
```
docker-compose up
```

### manually shell into db
```
psql -h localhost -U test -d postgres
```
