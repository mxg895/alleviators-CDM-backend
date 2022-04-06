from uuid import UUID
from app.resources.model import Resource, db
from flask import Blueprint, jsonify, make_response, request
from sqlalchemy.orm import load_only

resource = Blueprint('resource', __name__)

def updateNumMatch(resource, req_data):
  serialized_resource = resource.serialize_cover
  count = 0
  # aspectMatch = filter(lambda x: x in req_data.aspect , resource.aspect)
  aspect_match = [x for x in serialized_resource['aspect'] if x in req_data['aspect']]
  goal_match = [y for y in serialized_resource['goal'] if y in req_data['goal']]
  sub_cat_match = [z for z in serialized_resource['subcategory'] if z in req_data['subcategory']]
  
  count = len(aspect_match) + len(goal_match) + len(sub_cat_match)
  serialized_resource["matchCount"] = count
  
  return serialized_resource
  

@resource.route('/resource', methods=['POST'])
def sorted_resources():
  request_data = request.json
  if request_data is None:
    request_data = request.data
  if request_data is None:
    return jsonify("Request body for getting curated content is Null!"), 404
  all_Resources = Resource.query.options(load_only(
    Resource.id,
    Resource.title,
    Resource.aspect,
    Resource.goal,
    Resource.sub_category,
    Resource.image_name)).all()

  serial_updated_rs = [updateNumMatch(r, request_data) for r in all_Resources]
  serial_updated_rs.sort(key=lambda x: x['matchCount'], reverse=True)
  return jsonify(serial_updated_rs), 200

@resource.route('/resource/<string:resource_id>', methods=['GET'])
def resource_detail(resource_id):
  # return_val = jsonify(resource_details=resource_id)
  resource_detail = Resource.query.options(load_only(
    Resource.id,
    Resource.description,
    Resource.content,
    Resource.external_links
  )).get(resource_id)
  serialized_detail = resource_detail.serialize_detail
  return jsonify(serialized_detail), 200