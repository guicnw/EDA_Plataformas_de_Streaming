import numpy as np
import pandas as pd

class limpieza:
    def eliminar_nulos_title(self, df):
        return df.dropna(subset=["title"])

    def eliminar_duplicados_completos(self, df):
        return df.drop_duplicates()

    def eliminar_duplicados_title(self, df):
        return df.drop_duplicates(subset="title")

    def eliminar_columna_imdbId(self, df):
        return df.drop(columns=["imdbId"])
    
    def eliminar_filas_con_muchos_nulos(self, df):
        max_nulos = len(df.columns) - 2
        return df.dropna(thresh=max_nulos)
    
    def eliminar_filas_con_genres_nulo(self, df):
        return df.dropna(subset=["genres"])

    def rellenar_nulos_mejorada(self, df, columna):
        grupos = df['type'].unique()
        for grupo in grupos:
            media = df[df['type'] == grupo][columna].mean()
            std = df[df['type'] == grupo][columna].std()
            n_nulos = len(df[(df['type'] == grupo) & (df[columna].isna())])
            df.loc[(df['type'] == grupo) & (df[columna].isna()), columna] = np.random.normal(media, std, n_nulos)
        return df
    

    def limpiar_dataset(self, df):
        df = self.eliminar_nulos_title(df)
        df = self.eliminar_duplicados_completos(df)
        df = self.eliminar_duplicados_title(df)
        df = self.eliminar_columna_imdbId(df)
        df = self.eliminar_filas_con_muchos_nulos(df)
        df = self.eliminar_filas_con_genres_nulo(df)
        df = self.rellenar_nulos_mejorada(df, 'imdbAverageRating')
        df = self.rellenar_nulos_mejorada(df, 'imdbNumVotes')
        return df