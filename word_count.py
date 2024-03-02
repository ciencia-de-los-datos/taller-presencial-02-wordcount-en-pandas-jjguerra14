"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    # filenames=glob.glob(f"{input_directory}/*.txt")
    # dataframes=[]
    # for filename in filenames:
    #     dataframes.append(pd.read_csv(filename,sep="\t, header=None, names ["text"]"))

    # dataframes =  [
    #     pd.read_csv(filename, sep="\t", header=None, names=["text"])
    #     for filename in filenames
    # ]
    # return dataframes
    filenames = glob.glob(f"{input_directory}/*.txt")

    # dataframes = []
    # for filename in filenames:
    #     dataframes.append(pd.read_csv(filename, sep="\t", header=None, names=["text"]))
    dataframes = [
        pd.read_csv(filename, sep="\t", header=None, names=["text"])
        for filename in filenames
    ]

    concatenated_df=pd.concat(dataframes, ignore_index=True)
    return concatenated_df

def clean_text(dataframe):
    # df=pd.read_csv(filenames[0],sep="\t",header=None, names=["text"])
# print(df)
    dataframe=dataframe.copy()
    dataframe["text"]=dataframe["text"].str.lower()
    dataframe["text"]=dataframe["text"].str.replace(",","")
    dataframe["text"]=dataframe["text"].str.replace(".","")
    return dataframe
    #convertir a mayusculas o a minusculas, eliminar acentos 
    #eliminar puntuación




def count_words(dataframe):
    """Word count"""
    dataframe=dataframe.copy()
    dataframe["text"]=dataframe["text"].str.split()
    dataframe=  dataframe.explode("text")
    dataframe=dataframe["text"].value_counts()
    #dataframe["count"]=1

    #dataframe=dataframe.groupby("text",as_index=False).agg({"count":"sum"})
    return dataframe


def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, sep="\t",index=True,header=False)

    return dataframe

df=load_input("input")
df=clean_text(df)
df=count_words(df)
save_output(df,"output.txt")
print(df)

# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    df=load_input(input_directory)
    df=clean_text(df)
    df=count_words(df)
    save_output(df,"output.txt")



# if __name__ == "__main__":
#     run(
#         "input",
#         "output.txt",
#     )
