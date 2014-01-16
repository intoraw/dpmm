import numpy as np
import pprint

GEN_DATA_SCALE = 1.0

class Data():
  xdata = {}
  ydata = {}
  mdid = 1
  mcid = 1
  belogs = {}  # data id -> class id
  contains = {}  # class id -> data id list


  def __init__(self):
    pass


  @staticmethod
  def add_data(x_value, y_value):
    """
      x_value : x value, double
      y_value : y value, double
      return : data id
    """
    _id = Data.mdid
    Data.xdata[_id] = x_value
    Data.ydata[_id] = y_value
    Data.mdid += 1
    return _id
    

  @staticmethod
  def gen_data(data_size, class_size, gauss_mean):
    """
      data_size : each class data size
      class_size : class number
      gauss_mean : a list, [(x_mean, y_mean), ... ]
      return : None, initialize data to xdata and ydata
    """ 
    for _cid in range(class_size):
      x_mean, y_mean = gauss_mean[_cid]
      x_value = np.random.normal(x_mean, GEN_DATA_SCALE, data_size)
      y_value = np.random.normal(y_mean, GEN_DATA_SCALE, data_size)
      for _i in range(data_size) :
        Data.add_data(x_value[_i], y_value[_i])


  @staticmethod
  def getxdata(did):
    """
      did : data id
      return : x data of that id
    """
    if did not in Data.xdata.keys():
      return None
    return Data.xdata[did]

  
  @staticmethod
  def getydata(did):
    """
      did : data id
      return : y data of that id
    """
    if did not in Data.ydata.keys():
      return None
    return Data.ydata[did]

  @staticmethod
  def get_all_data_id():
    """
      return : all data id
    """
    return Data.xdata.keys()


  @staticmethod
  def get_all_class_id():
    """
      return : class id list
    """
    return list(set(Data.belogs.values()))

  
  @staticmethod
  def get_data_class(did):
    """
      did : data id
      return : class id
    """
    if did not in Data.belogs.keys():
      return None
    return Data.belogs[did]


  @staticmethod
  def get_class_data(cid):
    """
      cid : class id
      return : data id list []
    """
    if cid not in Data.contains.keys():
      return None
    return Data.contains[cid]


  @staticmethod
  def new_class():
    """
      return : new class id
    """
    _cid = Data.mcid
    Data.mcid += 1
    Data.contains[_cid] = []
    return _cid


  @staticmethod
  def delete_class(cid):
    del Data.contains[cid]


  @staticmethod
  def mark(did, cid):
    """
      did : data id
      return : None. add data id to class
    """
    Data.belogs[did] = cid
    Data.contains[cid].append(did)


  @staticmethod
  def unlink_data(did):
    #del Data.xdata[did]
    #del Data.ydata[did]
    cid = Data.belogs[did]
    del Data.belogs[did]
    Data.contains[cid].remove(did)

  
  @staticmethod
  def get_data_id_after(did):
    ret = []
    all_ids = Data.xdata.keys()
    for _id in all_ids:
      if _id >= did :
        ret.append(_id)

    return ret


  @staticmethod
  def print_data():
    print(" [ xdata ] ")
    pprint.pprint(Data.xdata)
    print(" [ ydata ] ")
    pprint.pprint(Data.ydata)
    print(" [ belongs ] " )
    pprint.pprint(Data.belogs)
    print(" [ contains ] ")
    pprint.pprint(Data.contains)
    
    

def main():
  data_size = 10
  class_size = 3
  gauss_mean = [ (2,2) , (4,4), (0,0)]

  Data.gen_data(data_size, class_size, gauss_mean)
  
  print (Data.xdata)
  print (Data.ydata)



if __name__ == "__main__":
  main()


