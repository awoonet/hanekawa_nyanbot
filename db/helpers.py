class Helpers:
  @classmethod
  def find_or_create(cls, **params):
    instance = cls.get(id=params['id'])
    if instance:
      return instance
    return cls(**params)
