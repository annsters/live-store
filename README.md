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
to switch back to this virtualenv later, use
```
pyenv activate store-server
```
### client
```
npm install
```
then, click "run in web browser" on expo cli

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
password is test
