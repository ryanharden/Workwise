from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.models import db, Workspace, User
from backend.forms import workspace_form
import datetime

workspace_routes = Blueprint('workspaces', __name__)

def validation_errors_to_error_messages(validation_errors):
  """
  Simple function that turns the WTForms validation errors into a simple list
  """
  errorMessages = []
  for field in validation_errors:
    for error in validation_errors[field]:
      errorMessages.append(f'{field} : {error}')
  return errorMessages

# GET All Workspaces
@workspace_routes.route('')
@login_required
def get_all_workspaces():
    """
        Query for all workspaces and returns a list of workspace dictionaries
    """

    workspaces = Workspace.query.all()

    return {"workspaces": {workspace.id:workspace.to_dict() for workspace in workspaces}}


# GET All Workspaces by User
@workspace_routes.route("/user")
@login_required
def get_user_workspaces():
    user = current_user

    if not user:
        return {"errors": "User not found"}, 404

    workspaces = user.workspaces
    return { workspace.id: workspace.to_dict() for workspace in workspaces }


# GET Workspace by ID
@workspace_routes.route("/<int:id>")
@login_required
def get_workspace_by_id(id):
    """
        Query for a workspaces by ID and returns it as a dictionary    """
    workspace =Workspace.query.get(id)

    if not workspace:
        return {"errors": "Workspace not found"}, 404

    workspace_dict = workspace.to_dict()

    return workspace_dict


# POST: Create a New Workspace
@workspace_routes.route("", methods=["POST"])
@login_required
def create_workspace():
    form = workspace_form()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        workspace = Workspace(
            name = form.data['name'],
            description = form.data["description"],
            owner_id = current_user.id,
            visibility = form.data['visbility'],
            created_at = datetime.datetime.utcnow()
        )

        db.session.add(workspace)
        db.session.commit()

        return workspace.to_dict()

    if form.errors:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 400



# PUT: Update a Workspace by ID
@workspace_routes.route("/<int:id>", methods=["PUT"])
@login_required
def edit_workspace(id):
    """
        Query a specific workspace by ID and update it with values given by the user. Return a dictionary of the updated workspace
    """

    workspace = Workspace.query.get(id)

    if not workspace:
        return {"errors":"Workspace not found"}, 404

    form = workspace_form()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        workspace.name = form.data['name']
        workspace.description = form.data["description"]
        workspace.visibility = form.data['visbility']

        db.session.add(workspace)
        db.session.commit()

        return workspace.to_dict()
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 400



# DELETE a workspace by ID
@workspace_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_workspace(id):
    workspace = Workspace.query.get(id)

    if not workspace:
        return { "errors: ", "Workspace not found" }

    db.session.delete(workspace)
    db.session.commit()

    return { "message": "Delete successful" }
