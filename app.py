# Core pkgs
import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import altair as alt
from datetime import datetime

#online ml pkgs
from river.naive_bayes import MultinomialNB
from river.feature_extraction import BagOfWords,TFIDF
from river.compose import Pipeline


# Training Data
data = [("my unit test failed","software"),
("tried the program, but it was buggy","software"),
("i need a new power supply","hardware"),
("the drive has a 2TB capacity","hardware"),
("unit-tests","software"),
("program","software"),
("power supply","hardware"),
("drive","hardware"),
("it needs more memory","hardware"),
("check the API","software"),
("design the API","software"),
("they need more CPU","hardware"),
("code","software"),
("i found some bugs in the code","software"),
("i swapped the memory","hardware"),
("i tested the code","software")]

<!------------>









# Create Fxn from SQL 

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS predictionTable(message TEXT,prediction TEXT, probability NUMBER,software_proba NUMBER,hardware_proba NUMBER, postdate DATE)')

def add_data(message,prediction,probability,software_proba,hardware_proba,postdate):
    c.execute('INSERT INTO predictionTable(message,prediction,probability,software_proba,hardware_proba,postdate) VALUES (?,?,?,?,?,?)',(message,prediction,probability,software_proba,hardware_proba,postdate))
    conn.commit()

def view_all_data():
    c.execute("SELECT * FROM predictionTable")
    data = c.fetchall()
    return data



st.write("""
# ML app for prediction of Text as Hardware/Software related
*Machine Learning on streaming data in Python with River*
""")


def main():
    menu = ["Home", "Manage", "About"]
    create_table()

    <!---------->
      

if __name__ == '__main__':
    main()
