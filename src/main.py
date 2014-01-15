from data import Data
from crp  import CRP

def main():
  
  # Data generation settting
  data_size = 100
  class_size = 3
  gauss_mean = [ (2,2), (0,0), (4,4) ]

  # DPMM setting
  alpha = 0.5


  # Generate data
  Data.gen_data(data_size, class_size, gauss_mean)

  # Random partition data
  CRP.alpha = alpha
  CRP.init_partition()
  
  Data.print_data()

  # Test



if __name__ == '__main__':
  main()

