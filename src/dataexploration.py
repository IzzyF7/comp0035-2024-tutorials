from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def sample_histogram(df):
    """Draw a sample plot using pandas.plot() method.

    Args:
        df (pd.DataFrame): Sample DataFrame to plot.

    Returns:
        None
    """
    #display a figure with distributions of the data
    #df.hist()

    # Show the plot
    #plt.show()
    
    #display specific columns
    #df['duration'].hist()
    #plt.show()

    #create histograms for the winter and summer events.
    #summer_df = df[df['type'] == 'summer']
    #summer_df.hist()
    #winter_df = df[df['type'] == 'winter']
    #winter_df.hist()
    #plt.show()

    return df

#generate a box plot   
def sample_boxplot(df):
    """Draw a sample boxplot using pandas.plot() method and save to .png file.

    Args:
        df (pd.DataFrame): Sample DataFrame to plot.

    Returns:
        None

    """
    #df.boxplot()
    #subplots
    #df.plot.box(subplots=True, sharey=False)
    #plt.savefig('bp_example.png')
    #plt.show()
    return df

def sample_lineplot(df):
    """Draw a sample line plot using pandas.plot() method.

    Args:
        df (pd.DataFrame): Sample DataFrame to plot.

    Returns:
        None

    """
    #sort df by the start column
    df = df.sort_values(by='start')
    #group the data by the type column
    df = df.groupby('type')
    #create a plot where x="start" and y="participants"
    df.plot(x='start', y='participants')
    plt.show()
    return df
    

if __name__ == '__main__':                  
    project_root = Path(__file__).parent
    csv_file = project_root.joinpath('tutorialpkg', 'data', 'paralympics_events_prepared.csv')

    # Load the prepared data
    df = pd.read_csv(csv_file)
    sample_histogram(df)
    sample_boxplot(df)
    sample_lineplot(df)
    