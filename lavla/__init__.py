import os




__version__ = "0.01-dev"
#
source = ""
f = ""

c_PAGE_NAME = ""
c_PAGE_ALIAS = ""


class lavla:
  _page_name = c_PAGE_NAME
  
  
  def __init__(name,path):
    path = os.path.join(path,name)
    if not os.path.exists(path):
      os.makedirs(path)
    f = open(path,"a")
    if f == None:
      print("Please add source.")
      
    f.format(page)
      
  def source(data)
    source = data
