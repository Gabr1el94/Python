from app import create_app,db
from flask_migrate import Migrate
from app.models import Contact, User

# flask shell -- ativar o terminal flask
# export FLASK_APP=main.py -- execução principal
# export FLASK_ENV=development -- módulo ambiente dev
# flask run -- executar o servidor

# flask db init -- inicialização repositório migração DB
# flask db migrate -- migração inicial DB 
# flask db upgrade -- aplicar migração ao DB

# Referência da Instância
app = create_app('development')

Migrate(app,db)

#Utilidade para terminal dinâmico do shell
@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Contact=Contact
    )
