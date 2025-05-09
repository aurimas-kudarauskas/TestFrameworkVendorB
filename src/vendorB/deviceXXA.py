class DeviceXXA:
  def __init__(self):
    pass

  def print_hello(self) -> None:
    print("Hi I am a device XXA from Vendor B")

  def print_msg(self, msg:str) -> None:
    self.print_hello()
    print(msg)