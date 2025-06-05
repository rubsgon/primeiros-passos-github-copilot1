"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
   "Clube de Xadrez": {
      "description": "Aprenda estratégias e participe de torneios de xadrez",
      "schedule": "Sextas, 15h30 - 17h",
      "max_participants": 12,
      "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
   },
   "Aula de Programação": {
      "description": "Aprenda fundamentos de programação e desenvolva projetos de software",
      "schedule": "Terças e quintas, 15h30 - 16h30",
      "max_participants": 20,
      "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
   },
   "Educação Física": {
      "description": "Educação física e atividades esportivas",
      "schedule": "Segundas, quartas e sextas, 14h - 15h",
      "max_participants": 30,
      "participants": ["john@mergington.edu", "olivia@mergington.edu"]
   },
   # Esportivas
   "Futebol": {
      "description": "Treinos e partidas de futebol para todos os níveis",
      "schedule": "Terças e quintas, 16h - 17h30",
      "max_participants": 22,
      "participants": ["lucas@mergington.edu", "marcos@mergington.edu"]
   },
   "Vôlei": {
      "description": "Aulas e jogos de vôlei para iniciantes e avançados",
      "schedule": "Quartas e sextas, 15h - 16h30",
      "max_participants": 14,
      "participants": ["ana@mergington.edu", "carla@mergington.edu"]
   },
   # Artísticas
   "Teatro": {
      "description": "Expressão corporal, atuação e produção de peças teatrais",
      "schedule": "Segundas e quartas, 17h - 18h30",
      "max_participants": 18,
      "participants": ["paulo@mergington.edu", "juliana@mergington.edu"]
   },
   "Oficina de Pintura": {
      "description": "Técnicas de pintura em tela e exposições artísticas",
      "schedule": "Sábados, 10h - 12h",
      "max_participants": 15,
      "participants": ["lara@mergington.edu", "renato@mergington.edu"]
   },
   # Intelectuais
   "Clube de Leitura": {
      "description": "Leitura e discussão de livros clássicos e contemporâneos",
      "schedule": "Quartas, 16h - 17h",
      "max_participants": 16,
      "participants": ["camila@mergington.edu", "rodrigo@mergington.edu"]
   },
   "Olimpíada de Matemática": {
      "description": "Preparação para olimpíadas e desafios matemáticos",
      "schedule": "Sábados, 8h - 10h",
      "max_participants": 25,
      "participants": ["bruno@mergington.edu", "aline@mergington.edu"]
   }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    # Validar se o estudante já está inscrito
      if email in [participant for activity in activities.values() for participant in activity["participants"]]:
         raise HTTPException(status_code=400, detail="Estudante já inscrito nesta atividade")
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")

    # Get the specificy activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"{email} inscrito(a) em {activity_name} com sucesso"}
