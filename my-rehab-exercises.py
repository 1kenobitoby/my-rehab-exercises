import streamlit as st
import time
import random
import pandas as pd

st.set_page_config(
    page_title="My rehab exercises",
    page_icon="images/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
    #menu_items={
        #'Get Help': '<<URL>>',
        #'Report a bug': "<<URL>>",
        #'About': "Made with Streamlit v1.27"
    #}
)

# Get struct_time and strip full weekday name from it (%A)
day=time.strftime("%A", time.localtime())


st.image('images/logo.svg', width=100)
st.header(day + "'s exercises")

# a dictionary of 3 lists: 1. Exercise names; 2. Video URLs showing how to perform the exercises; 3. The start time in seconds of the relevant bit in the video
database={
    'Exercise name': ["Curl up", "Bird dog", "Side plank", "Knee off bed", "Scorpion roll", "SI joint corkscrew", "Windscreen/piriformis rolls", "Tennis ball release", "Donkey kicks", "90:90 sacrum lifts", "Wall sits", "Single leg squats", "Clam shells", "Fire hydrants", "Bridges/thrusts/donkey kicks", "SL abduction", "90 wall ball roll", "Ball-wall deadlift"],
    'Video':["https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=Qhk6nrorgT8"],
    'Start time':[68, 295, 205, 58, 323, 446, 603, 71, 524, 169, 377, 686, 474, 490, 505, 524, 279, 396]
}

# Pass database to pandas dataframe constructor to make 'table'
# Table has a row for each exercise showing name, video URL and start time in video
table = pd.DataFrame(database)

#table

# pick 6 rows at random from 18 and put in list 'exercises'
exercises = random.sample(range(0,18), 6)
#exercises

#initialise counter 'number'
number=0

# Loop through pulling the exercise name from column 1 to put in the Streamlit tab called tab_text
# then pull the associated video URL from column 2 and set the start time from column 3
for i in exercises:
    number +=1
    tab_text, tab_video = st.tabs(["Exercise " + "%.0f" % number, "Video"])
    with tab_text:
        st.write(f"**{table.iloc[i, 0]}**")
        st.write("\n")

    with tab_video:
        st.video(table.iloc[i, 1], start_time=table.iloc[i,2]) 

st.divider()

# Some gym workout schedules and YouTube stretching routines, 1 for each day of the week, to follow.
st.header('Today\'s workout')

if day=="Saturday":
    st.image('images/day_1.png')
if day=="Sunday":
    st.vidoe("https://www.youtube.com/watch?v=0arLyM00F_w")    
elif day=="Monday":
    st.video('https://www.youtube.com/watch?v=FX-R98zU5MI')
elif day=="Tuesday":
    st.image('images/day_2.png')
elif day=="Wendesday":
    st.image('https://www.youtube.com/watch?v=ui3ToKZtKIs', start_time=30)
elif day=="Thursday":
    st.image('images/day_3.png')
else:
    st.video('https://www.youtube.com/watch?v=FX-R98zU5MI')    


