import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import pandas as pd
import click

@click.group()
def cli():
    """Systemtrader analyze trade information"""
    pass

@cli.command('N225')
def show_N225():
    """Retrieve and analyze NIKKEI225 trade history from fred."""    
    N225 = pdr.DataReader("NIKKEI225", 'fred')
    N225.plot(color='darkblue')
    plt.ylabel('N225 index')
    plt.show()
    return

@cli.command('DEXJPUS')
def show_DEXJPUS():
    """Retrieve and analyze DEXJPUS trade history from fred."""
    fx = pdr.DataReader('DEXJPUS', 'fred')
    price = pdr.DataReader('NIKKEI225', 'fred')
    #port = pd.concat([price.Close, fx], axis=1).dropna()
    port = pd.concat([price, fx], axis=1).dropna()
    n = port.NIKKEI225.pct_change().dropna()
    f = port.DEXJPUS.pct_change().dropna()
    f.rolling(window=20).corr(n).plot(color="yellow")
    plt.ylabel('correlation')
    plt.show()
    return

if __name__ == "__main__":
    cli()
