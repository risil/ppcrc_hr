from flask.views import MethodView
from flask_smorest import Blueprint
from myapp.response import APIResponse
from myapp.data_schema.schema import ManagerSchema
from myapp.model.models import Manager
from uuid import uuid4

managers_blueprint = Blueprint("managers", __name__, url_prefix="/api", description="Manager Operations")

@managers_blueprint.route('/managers')
class Managers(MethodView):

    def get(self):
        managers = Manager.objects().all()
        return APIResponse.respond(managers, "Successful", 200)

    @managers_blueprint.arguments(ManagerSchema)
    def post(self, manager_data):
        manager = Manager(
            _id=str(uuid4().hex),
            user=manager_data.get("user"),
            designation=manager_data.get("designation"),
            created_at=None,
            created_by=None,
            updated_at=None,
            updated_by=None,
            is_deleted=0
        )
        manager.save()
        return APIResponse.respond(manager, "Manager created successfully", 200)
