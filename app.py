from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "hola render"
    servicios_veloce = [
        {'id': 'ser1', 'nombre': 'Documentación Confidencial', 'info': 'Manejo seguro de sobres y documentos legales.'},
        {'id': 'ser2', 'nombre': 'Logística para E-commerce', 'info': 'Entregas estratégicas para tiendas en línea.'},
        {'id': 'ser3', 'nombre': 'Envíos Urgentes Expreso', 'info': 'Entregas prioritarias en tiempo récord.'},
        {'id': 'ser4', 'nombre': 'Artículos de Almacenaje', 'info': 'Gestión y transporte de mercadería delicada.'},
        {'id': 'ser5', 'nombre': 'Tramites', 'info': 'Gestiones administrativas y pagos generales.'}
    ]
    socios = ["Nacional Seguros", "Paceña", "PIL", "Notaria 101", "Sudamericana", "Optica Vision Mundial"]
    return render_template('servicios.html', servicios=servicios_veloce, socios=socios)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        return render_template('contacto.html', enviado=True, nombre=nombre)
    return render_template('contacto.html', enviado=False)

if __name__ == '__main__':
    app.run()