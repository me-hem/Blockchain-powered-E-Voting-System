from app import app
import sys

app.secret_key = '6dbf23122cb5046cc5c0c1b245c75f8e43c59ca8ffeac292715e5078e631d0c9'
app.config['SESSION_TYPE'] = 'filesystem'

port = sys.argv[1]

app.run(debug=True, port=port)
