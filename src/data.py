import numpy as np

GEN_DATA_SCALE = 1.0


class Data():
  xdata = {}
  ydata = {}
  mdid = 0

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
    return Data.xdata[did]

  
  @staticmethod
  def getydata(did):
    """
      did : data id
      return : y data of that id
    """
    return Dataydata[did]

  @staticmethod
  def get_all_id():
    """
      return : all data id
    """
    return Data.xdata.keys()

def main():
  data_size = 10
  class_size = 3
  gauss_mean = [ (2,2) , (4,4), (0,0)]

  Data.gen_data(data_size, class_size, gauss_mean)
  
  print (Data.xdata)
  print (Data.ydata)



if __name__ == "__main__":
  main()


