from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.models import db, Project, User
from backend.forms import ProjectForm
import datetime

project_routes = Blueprint('projects', __name__)

def validation_errors_to_error_messages(validation_errors):
  """
  Simple function that turns the WTForms validation errors into a simple list
  """
  errorMessages = []
  for field in validation_errors:
    for error in validation_errors[field]:
      errorMessages.append(f'{field} : {error}')
  return errorMessages


# GET All Projects
@project_routes.route('')
@login_required
def get_all_projects():
    """
        Query for all projects and returns a list of project dictionaries
    """

    projects = Project.query.all()

    return { project.id: project.to_dict() for project in projects }

# GET All Project by User
@project_routes.route('/user')
@login_required
def get_all_user_projects():
    """
        Query for all user projects and returns a list of project dictionaries
    """

    projects = Project.query.filter(Project.owner_id==current_user.id).all()

    return { project.id: project.to_dict() for project in projects }

# GET Project by ID
@project_routes.route('/<int:id>')
def get_project(id):
  project = Project.query.get(id)

  if not project:
    return {"errors: ", "Project Not Found"}, 404

  return project.to_dict()



# POST - Create a new project
@project_routes.route('', methods=['POST'])
@login_required
def create_project():
  form =ProjectForm()
  form['csrf_token'].data = request.cookies['csrf_token']
  if form.validate_on_submit():
    project =Project(
      workspace_id=form.data['workspace_id'],
      owner_id= current_user.id,
      name=form.data['name'],
      description = form.data['description']
    )

    db.session.add(project)
    db.session.commit()

    return project.to_dict()
  if form.errors:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 400


# PUT - Edit Project
@project_routes.route("/<int:id>", methods=["PUT"])
@login_required
def edit_project(id):
    project = Project.query.get(id)

    if not project:
      return {"errors: ", "Project Not Found"}, 404

    form = ProjectForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        form.populate_obj(project)

        db.session.add(project)
        db.session.commit()
        return project.to_dict()
    if form.errors:
       return {"errors": validation_errors_to_error_messages(form.errors)}, 400

# DELETE a Project by ID
@project_routes.route('/<int:id>', methods=["DELETE"])

@login_required
def delete_project(id):
    project = Project.query.get(id)

    if not project:
        return {'errors': "Project not found." }, 400

    if not current_user.id == project.owner_id:
        return {"errors":"User authorized to delete project."}, 400

    db.session.delete(project)
    db.session.commit()

    return {"message": "Delete successful"}
