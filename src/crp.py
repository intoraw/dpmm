from data import Data
from mathutils import prob_based_rand

ALPHA = 0.5


class CRP():

  alpha = ALPHA

  def __init__(self):
    pass

 
  @staticmethod
  def init_partition():
    """
      return : None . init partitions 
    """
    # Random initialize class
    data_size = len(Data.xdata)
    for _i in range(data_size):
      Data.new_class()
  
    probs = [ 1.0 / data_size for _ in range(data_size) ]

    for _id in Data.get_all_data_id() :
      _cid = prob_based_rand(probs)
      Data.mark(_id, _cid)

