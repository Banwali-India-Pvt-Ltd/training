class NonNegativeInt(object):
   def __init__(self, value):
     if value < 0:
       raise Exception("Hey, what the...")
     self.value = value

   def __eq__(self, that):
     if isinstance(that, int):
       return self.value == that
     elif isinstance(that, NonNegativeInt):
       return self.value == that.value
     else:
       raise ArgumentError("Not an acceptible argument", "__eq__", that)