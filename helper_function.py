import pandas as pd

def time_as_independent_variable(microarray_df):
    """
    uses basic pandas functionality to reformat dataframe for different use case
    df: type(pd.DataFrame) - split columns into multiple rows as time measurements
    """
    columns = microarray_df.columns.tolist()
    times = ['[00m]', '[05m]', '[15m]']

    protein_features = [column for column in columns if column.startswith('p')]
    overall_features = [column for column in columns if not column.startswith('p')]

    time_df_dict = {}

    for time in times:
        time_features = [protein for protein in protein_features if protein.endswith(time)]
        time_df = microarray_df[overall_features + time_features].copy(deep=True)
        time_df['Time'] = int(time[1:3])
        new_column_order = time_df.columns.tolist()
        new_column_order.insert(0, new_column_order.pop())

        time_df = time_df[new_column_order]
        new_column_names = [feature.replace(time, '').strip() for feature in time_df.columns.tolist()]
        time_df_dict[time] = pd.DataFrame(time_df.values, columns = new_column_names)


    df_list = [item for _, item in time_df_dict.items()]
    new_df = pd.concat(df_list, sort=False, ignore_index=True)
    return new_df
