# import packages
# show the title
# read csv and show the dataframe
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

# import packages and finish the task: read data, show title, draw 3 boxplots (15,5)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

sns.set_theme(style="darkgrid")
plt.rcParams["figure.figsize"] = (15, 5)

# read data
df = pd.read_csv("train.csv")

# show title
st.title("Titanic app by Xu Zilin")

#table
display_cols = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
st.dataframe(df[display_cols].round(2), use_container_width=True)

# create figure with three subplots and draw boxplots
ticket_price = df["Ticket"].dropna().sort_values(ascending=False).reset_index(drop=True)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

flierprops = {
    "marker": "o",
    "markerfacecolor": "white",
    "markeredgecolor": "black",
    "markersize": 6,
    "alpha": 0.6,
}
boxprops = {"facecolor": "#e6eef8", "edgecolor": "#4C72B0"}
medianprops = {"color": "red", "linewidth": 2}

for cls, ax in zip([1, 2, 3], axes):
    subset = df[df["Pclass"] == cls]
    sns.boxplot(
        x="Pclass",
        y="Fare",
        data=subset,
        ax=ax,
        boxprops=boxprops,
        flierprops=flierprops,
        medianprops=medianprops,
        showcaps=True,
        whiskerprops={"color": "#4C72B0"},
    )
    ax.set_title("")
    ax.set_xlabel(f"fare\nPClass = {cls}")
    if ax is axes[0]:
        ax.set_ylabel("Fare")
    else:
        ax.set_ylabel("")

plt.tight_layout()
plt.show()
st.pyplot(fig)

