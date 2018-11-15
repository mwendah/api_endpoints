from falsk import Blueprint
from flask_restful import Api
from App.api.v1.veiws import ParcelModel
from App.api.v1.veiws import DataParcel

version1=Blueprint('v1', __name__, url_prefix,/api)
Api=api(version1)
api.add_resource(DataDelivery,"/DataDelivery")
api.add_resource(singleDelivery,"/single/<int:id>")
api.add_resource(CancelDElivery,"/cancel/<int:id>")
api.add_resource(UserDElivery,"/user")
api.add_resource(GetUser,"/user/<int:username>")

@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route("/parcel", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)
