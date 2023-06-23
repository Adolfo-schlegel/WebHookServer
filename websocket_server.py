from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room

usuarios = []

class WebsocketServer:
    
    app = Flask(__name__)
    socketio = SocketIO(app, cors_allowed_origins='*')
    

    def __init__(self):
        print("Running...")        
        self.socketio.on_event('message', self.handle_message)

    @socketio.on('connect')
    def handle_connect():
        # Obtén el identificador único del usuario
        usuarios.append(request.sid)
        for usuario in usuarios:
            print('-----------------------------')
            print('Usuario conectado:', usuario)  
            print('-----------------------------')
    
    @socketio.on('message')
    def handle_message(self, message):
        # Obtén el identificador único del usuario
        user_id = request.sid

        print(user_id,' -> ', message)
        emit('message',user_id + ': ' + message, broadcast=True)

    @socketio.on('get_list')
    def handle_get_list():
        emit('list_users', usuarios)

    @socketio.on('disconnect')
    def handle_disconnect():

        # Obtén el identificador único del usuario
        user_id = request.sid
        
        # Cuando el usuario se desconecta lo elimino
        if user_id in usuarios:
            usuarios.remove(user_id)
        
        print('Usuario desconectado:', user_id)

    def run(self):
        self.socketio.run(self.app)

