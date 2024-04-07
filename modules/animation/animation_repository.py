from typing import List
from modules.animation.animation_domain import Animation

ANIMATIONS = [
  {'id': '0', 'name': 'The Simpsons', 'startDate': 1, 'finishDate': 2},
  {'id': '1', 'name': 'South Park', 'startDate': 1, 'finishDate': 2},
]

class AnimationRepository:
  
  def create(self, data) -> Animation:
    data_to_create = Animation(data)
    ANIMATIONS.append(data_to_create.__dict__)
    return data_to_create
  
  def find_all(self, ) -> List[Animation]:
    return [Animation(data) for data in ANIMATIONS]
  
  def find_by_id(self, id) -> Animation:
    data_found = next((data for data in ANIMATIONS if data['id'] == id), None)
    return Animation(data_found) if data_found else None
  
  def update_by_id(self, id, data_to_update) -> Animation:
    index_to_update = next((index for index, data in enumerate(ANIMATIONS) if data['id'] == id), None)
    ANIMATIONS[index_to_update] = Animation(data_to_update).__dict__
    return Animation(data_to_update)
  
  def delete_by_id(self, id) -> None:
    index_to_delete = next((index for index, data in enumerate(ANIMATIONS) if data['id'] == id), None)
    ANIMATIONS.pop(index_to_delete) if index_to_delete else None
