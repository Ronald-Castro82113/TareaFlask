import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://database_tarea_user:iDeOPJrXVhhUvqO5HUMdg7ieKSpfaOvd@dpg-d0dv60c9c44c73cei7c0-a.oregon-postgres.render.com:5432/database_tarea'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
