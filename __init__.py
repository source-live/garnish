import os

class website:
  wpath_ = ""
  def __init__(name,path):
    # Name is a string, path is an array: website(string name, array path)
    p = "/".join(path)
    pc = "".join(["C:/",p])
    os.mkdirs(pc)
    print("".join(["Successfully made website @ ",pc]))
    if name and path == None:
      return False
    else:
      return True
