from flask import Blueprint, request, render_template, redirect, url_for
from flask import flash, get_flashed_messages, redirect, url_for
#from app.models import Usuario, Libro
from app.models import Libro
from datetime import datetime
from app import db
from flask import jsonify


libros_bp = Blueprint("libros", __name__)

@libros_bp.route("/libros", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        editorial = request.form.get("editorial")

        nuevo_libro = Libro(titulo=titulo, autor=autor, editorial=editorial)

        db.session.add(nuevo_libro)
        db.session.commit()

        flash("Libro agregado correctamente", "success")
        return redirect(url_for("libros.users"))
        
    
    busqueda = request.args.get("buscar")
    if busqueda:
        libros = Libro.query.filter(
            (Libro.titulo.ilike(f"%{busqueda}%")) | (Libro.autor.ilike(f"%{busqueda}%"))
        ).all()

        if not libros:
            flash("No se encontró libro con este título o autor", "error")
            return redirect(url_for("libros.users"))
    else:
        libros = Libro.query.all()

    return render_template("index.html", productos = libros)
        
        
    
@libros_bp.route("/libros/eliminar/<int:id>", methods=["POST"])
def eliminar_libro(id):
    libro_a_eliminar = Libro.query.get(id)
    
    if libro_a_eliminar:
    
        db.session.delete(libro_a_eliminar)
        db.session.commit()
    
        flash("Libro eliminado correctamente", "success")
    
    else:
        flash("No se encontró el libro", "error")

    return redirect(url_for("libros.users"))

@libros_bp.route("/libros/editar/<int:id>", methods=["GET"])
def mostrar_formulario_edicion(id):
    libro = Libro.query.get_or_404(id)
    return render_template("editar.html", libro=libro)

@libros_bp.route("/libros/editar/<int:id>", methods=["POST"])
def actualizar_libro(id):
    libro = Libro.query.get_or_404(id)
    libro.titulo = request.form.get("titulo")
    libro.autor = request.form.get("autor")
    libro.editorial = request.form.get("editorial")

    db.session.commit()
    flash("Libro actualizado correctamente", "success")
    return redirect(url_for("libros.users"))