from flask import Flask, request
from flask.views import MethodView
from flask_smorest import Blueprint
from myapp.response import APIResponse
from myapp.data_schema.schema import ManagerSchema
from myapp.model.models import Manager

manager_blueprint = Blueprint("manager", __name__, url_prefix="/manager")

class ManagerResource(MethodView):
    @manager_blueprint.arguments(ManagerSchema)
    @manager_blueprint.response(201, ManagerSchema)
    def post(self, manager_data):
        manager = Manager(**manager_data)
        manager.save()
        return APIResponse.respond(manager.to_mongo().to_dict(), "Manager created successfully!", 201)

    @manager_blueprint.arguments(ManagerSchema)
    @manager_blueprint.response(200, ManagerSchema)
    def put(self, manager_data):
        manager_id = manager_data["_id"]
        manager = Manager.objects.get(_id=manager_id)
        manager.update(**manager_data)
        manager.reload()
        return APIResponse.respond(manager.to_mongo().to_dict(), "Manager updated successfully!", 200)

    @manager_blueprint.response(204)
    def delete(self, manager_id):
        manager = Manager.objects.get(_id=manager_id)
        manager.delete()
        return APIResponse.respond({}, "Manager deleted successfully!", 204)

    @manager_blueprint.response(200, ManagerSchema)
    def get(self, manager_id):
        manager = Manager.objects.get(_id=manager_id)
        return APIResponse.respond(manager.to_mongo().to_dict(), "Manager retrieved successfully!", 200)

    @manager_blueprint.response(200, ManagerSchema(many=True))
    def get_all(self):
        managers = Manager.objects.all()
        return APIResponse.respond(managers.to_mongo().to_dict(), "Managers retrieved successfully!", 200)

manager_blueprint.add_route(ManagerResource.as_view(), "/<manager_id>")
manager_blueprint.add_route(ManagerResource.as_view(), "")

app = Flask(__name__)
app.register_blueprint(manager_blueprint)

if __name__ == "__main__":
    app.run()
