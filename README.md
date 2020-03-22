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
docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres
```
