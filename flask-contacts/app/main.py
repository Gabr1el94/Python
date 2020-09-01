from app import create_app

# Referência da Instância
app = create_app('development')


#Utilidade para terminal dinâmico do shell
@app.shell_context_processor
def shell_context():
    return dict(

    )
