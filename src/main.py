from data import Data
from crp  import CRP

def main():
  
  # Data generation settting
  data_size = 100
  class_size = 3
  gauss_mean = [ (2,2), (0,0), (4,4) ]

  # DPMM setting
  alpha = 0.5
  niter = 10


  # Generate data
  Data.gen_data(data_size, class_size, gauss_mean)

  # Random partition data
  CRP.alpha = alpha
  CRP.init_partition()
  
  # Iterations
  for _it in range(niter):
    print "[ iteration %d ] ================" % (_it)
    
 


if __name__ == '__main__':
  main()

