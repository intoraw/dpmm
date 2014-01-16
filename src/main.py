from data import Data
from crp  import CRP
from evalue import Evalue

def main():
  
  # Data generation settting
  data_size = 100
  class_size = 3
  #gauss_mean = [ (2,2), (0,0), (4,4) ]
  gauss_mean = [ (2.4, 2), (-1.8, 1.4), (-0.2, -2.6)]

  # DPMM setting
  alpha = 0.5
  niter = 500


  # Generate data
  Data.gen_data(data_size, class_size, gauss_mean)

  # Random partition data
  CRP.alpha = alpha
  CRP.init_partition()
  
  # Iterations
  for _it in range(niter):
    print "[ iteration %d ] ================" % (_it)
    CRP.gibbs_sampling()
    Evalue.dovalue()
    
    print "[ evalueation %d ] ==============" % (_it)
    print "    cluster number : %d " % (len(Data.get_all_class_id()))
    print "    diff_class     : %f"  % (Evalue.diff_c[_it])
    print "    M_dis1         : %f"  % (Evalue.M_dis1[_it])
    print "    M_dis2         : %f"  % (Evalue.M_dis2[_it])

if __name__ == '__main__':
  main()

