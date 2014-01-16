from data import Data
from mathutils import prob_based_rand
from mathutils import prob_based_rand_dict
from mathutils import gauss_comp
import numpy as np
from numpy import transpose 

ALPHA = 0.5


class CRP():

  alpha = ALPHA
  probs = {}
  classpara = {} # key : class id, value : (x_para,y_para)

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
  
    _probs = [ 1.0 / data_size for _ in range(data_size) ]

    for _id in Data.get_all_data_id() :
      _cid = prob_based_rand(_probs) + 1
      Data.mark(_id, _cid)

  
  @staticmethod
  def get_classpara(cid):
    """
      cid : class id
      return : (x_para, y_para)
    """
    if cid not in CRP.classpara.keys():
      CRP.classpara[cid] = (0.0, 0.0)
    
    return CRP.classpara[cid]
 
  
  @staticmethod
  def _data_to_mat(did):
    """
      did : data id
      return : matrix 
    """
    x_value = Data.getxdata(did) 
    y_value = Data.getydata(did) 
    ret = np.zeros([1, 2], dtype=float)
    ret[0][0] = x_value
    ret[0][1] = y_value
    ret.shape = (1,2)
    return ret

  @staticmethod
  def _cpara_to_mat(cid):
    """
      cid : class id
      return : matrix 
    """
    if cid not in CRP.classpara.keys():
      CRP.classpara[cid] = (0.0, 0.0)
    x_para, y_para = CRP.classpara[cid]
    ret = np.zeros([1, 2], dtype=float)
    ret[0][0] = x_para
    ret[0][1] = y_para
    ret.shape = (1,2)
    return ret


  @staticmethod
  def gibbs_sampling():
    """
      do gibbs sampling
    """

    all_data_id = Data.get_all_data_id()
    perm = np.random.permutation(all_data_id)
    
    # Sample Z
    for _did in perm:
      CRP.probs.clear()
      _cid = Data.get_data_class(_did)
      Data.unlink_data(_did)
    
      all_class_id = Data.get_all_class_id()
      _data_mat = CRP._data_to_mat(_did)
      _data_size = len(Data.get_all_data_id())
      for __cid in all_class_id :
        __cpara_mat = CRP._cpara_to_mat(__cid)
        CRP.probs[__cid] = gauss_comp(transpose(_data_mat), transpose(__cpara_mat), 0, 'OLD')
        CRP.probs[__cid] = len(Data.get_class_data(__cid)) * CRP.probs[__cid] / (_data_size + CRP.alpha - 1)
 
      _new_cid = Data.new_class()
      CRP.probs[_new_cid] = CRP.alpha * gauss_comp(transpose(_data_mat), 0, 0, 'NEW') / ( _data_size + CRP.alpha - 1)

      # Sample
      _pre_cid = prob_based_rand_dict(CRP.probs)
      Data.mark(_did, _pre_cid)

      if _pre_cid != _new_cid :
        del CRP.probs[_new_cid]
        Data.delete_class(_new_cid)

    # Smaple Φ
    all_class_id = Data.get_all_class_id()
    CRP.classpara.clear()
    for _cid in all_class_id : 
      _class_data_id = Data.get_class_data(_cid)
      sigma = 1.0 / (1 + len(_class_data_id))
      x_values = [ Data.getxdata(__did) for __did in _class_data_id] 
      y_values = [ Data.getydata(__did) for __did in _class_data_id]
      mu_x , mu_y = sigma * np.sum(x_values) , sigma * np.sum(y_values)
      CRP.classpara[_cid] = ( np.random.normal(mu_x, sigma), np.random.normal(mu_y, sigma))








