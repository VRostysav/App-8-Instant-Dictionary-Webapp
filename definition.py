import pandas


class Definition:
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv('data.csv')
        definition = tuple(df.loc[df['word'] == self.term]['definition'])
        return definition


my_df = Definition('acid')
print(my_df.get())
