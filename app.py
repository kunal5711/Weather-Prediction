import streamlit as st
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import pickle
import sklearn
import warnings
warnings.filterwarnings("ignore")

org_data = pd.read_csv("Dataset/Weather.csv", nrows= 10)
df = pd.read_csv("Dataset/Weather_mod_dataset.csv", index_col='DATE', dayfirst=False, parse_dates=['DATE'])
df.index = pd.to_datetime(df.index, dayfirst=False, errors='coerce')
mod_data = df.iloc[0:10, :]

st.title("Weather Prediction")
nav = st.sidebar.selectbox("Navigation", ["Home", "Prediction"])

if (nav == "Home"):

    if st.checkbox("Original Data"):
        st.table(org_data)
    
    if st.checkbox("Modified Data"):
        st.table(mod_data)

    st.header("Visualization Plots")
    op = st.selectbox("Plots with Max temp", ["Monthly", "Yearly"])
    gr_monthly = df['tmax'].groupby(df.index.month).mean()
    gr_yearly = df['tmax'].groupby(df.index.year).mean()

    if op == "Monthly":
        fig2, ax2 = plt.subplots()
        ax2.plot(np.arange(0,12), gr_monthly)
        st.pyplot(fig2)

    if op == "Yearly":
        fig3, ax3 = plt.subplots()
        ax3.plot(np.arange(0,53), gr_yearly)
        st.pyplot(fig3)

if nav == "Prediction":
    st.subheader("Next 7 days Prediction")
    st.markdown('''<br>''', True)

    def date_decide(last_date, no_of_days):
        days = [last_date + datetime.timedelta(i) for i in range(1, no_of_days+1)]
        return pd.DataFrame({'DATE': days})

    last_date = df.index[-1]
    future_df = date_decide(last_date, 7)
    future_df.set_index('DATE', inplace=True)

    predi = ['tmax','tmin', 'rolling_3_tmax', 'rolling_3_tmin', 'month_avg_tmax', 'day_avg_tmax', 'month_avg_tmin', 'day_avg_tmin']
    
    # Initialize new columns in future_df
    for col in predi:
        future_df[col] = np.nan

    # Function to generate future predictions
    def future_preds(new_df, predictions, horizon):
        temp_df = df.tail(horizon).copy()  # Copy the last 'horizon' rows for rolling calculations
        temp_df.drop(['station', 'name', 'target'], axis=1, inplace=True)

        for i in range(len(new_df)):
            for col in predictions:
                rolling_mean = temp_df[col].rolling(horizon).mean().iloc[-1]  # Calculate rolling mean

                new_df[col].iloc[i] = rolling_mean  # Update new_df with the rolling mean

                # Add the new value to temp_df for the next rolling calculation
                next_index = new_df.index[i]
                temp_df.loc[next_index] = temp_df.iloc[-1].copy()
                temp_df.at[next_index, col] = rolling_mean

    rr = pickle.load(open('rr_model.sav', 'rb'))

    # Generate future predictions
    future_preds(future_df, predi, 3)
    preds = rr.predict(future_df)
    preds = pd.Series(preds, index = future_df.index)
    future_df['target'] = preds

    if st.checkbox("Last rows of data"):
        st.table(df.tail(5))

    input_date = st.date_input("Day")
    input_date = pd.Timestamp(input_date)
    st.write(input_date)

    if st.button("Predict"):

        if input_date in df.index:
            result = df.loc[input_date]['target']
            st.success(f"Maximum temp: {result}")

        elif input_date in future_df.index:
            result = future_df.loc[input_date]['target']
            st.success(f"Maximum temp: {round(result,2)}")
        
        else:
            st.error("You can only predict next 7 days from dataset.")
