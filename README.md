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
start server
```
cd server
python server.py
```
start client
```
npm install
npm start
```
then, click "run in web browser" on expo cli
