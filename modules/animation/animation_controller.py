from flask_restx import Namespace, Resource, fields
from modules.animation.animation_domain import Animation
from modules.animation.animation_repository import AnimationRepository

api = Namespace('animations', description='Animation related operations')
animation = api.model('Animation', {
  'id': fields.String(required=True, description='The animation identifier'),
  'name': fields.String(required=True, description='The animation name'),
  'startDate': fields.Integer(required=False),
  'finishDate': fields.Integer(required=False),
})

repository = AnimationRepository()

@api.route('/')
class AnimationController(Resource):
  @api.marshal_with(animation)
  @api.expect(animation)
  def post(self):
    return repository.create(api.payload)
    
  @api.marshal_list_with(animation)
  def get(self):
    return repository.find_all()
  
    

@api.route('/<id>')
@api.param('id', 'The animation identifier')
class AnimationItemController(Resource):
  @api.marshal_with(animation)
  def get(self, id):
    return repository.find_by_id(id)
  
  @api.marshal_with(animation)
  @api.expect(animation)
  def patch(self, id):
    return repository.update_by_id(id, api.payload)
      
  @api.marshal_with(animation)
  def delete(self, id):
    return repository.delete_by_id(id)