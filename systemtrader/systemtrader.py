import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

if __name__ == "__main__":
    N225 = pdr.DataReader("NIKKEI225", 'fred')
    N225.plot(color='darkblue')
    plt.ylabel('N225 index')
    plt.show()
