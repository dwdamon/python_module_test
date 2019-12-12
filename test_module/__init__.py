import uuid

name = "test_module"

class UUIDGenerator:
  def __init__(self, type):
    if type != 1 and type != 4:
      raise Exception( f"Unsupported UUIDGenerator type {type}.  Must be 1 or 4" )

    self._type = type

  def generate(self):
    retval = None

    if self._type == 1:
      retval = uuid.uuid1()
    elif self._type == 4:
      retval = uuid.uuid4()

    return retval

def test():
  generator1 = UUIDGenerator(1)
  generator4 = UUIDGenerator(4)
  print( f"Type 1: {generator1.generate()}" )
  print( f"Type 4: {generator4.generate()}" )
