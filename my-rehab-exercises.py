import streamlit as st
import time
import random
import pandas as pd

# pick 4 rows at random from number of rows in 'table' (i.e. range(0, len(table)) ) and put in list 'choices'
# cache data so it only runs 1st time and doesn't re-run every time user clicks something
# only cache the data for half an hour (ttl=1800) so all users aren't stuck with the same exercises forever
@st.cache_data(ttl=1800)
def choose():
    choices = random.sample(range(0,len(table)), 4)
    return choices

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

st.header(day + "'s morning workout")
if day=="Saturday":
    st.write('Tai chi')
    st.video("https://www.youtube.com/watch?v=NsZaY-EMpiA")
    st.write('More at [this playlist](https://www.youtube.com/playlist?list=PLMd1sFT4IdyZfsMxiILGDQRha1pPHb3pT)')
elif day=="Sunday":
    st.write('Gym work')   
elif day=="Monday":
    st.write('Resistance band workout')
    st.video('https://www.youtube.com/watch?v=mdFM2msfsbw')
elif day=="Tuesday":
    st.write('Pilates')
    st.video('https://www.youtube.com/watch?v=nnt34RN74Rs&list=PLipSZg1JNsC9DZcCHkgjHwIIP1jMnRrr0')
elif day=="Wednesday":
    st.write('Gym work')
elif day=="Thursday":
    st.write('Suspension training')
    st.video('https://www.youtube.com/watch?v=ohvltD4Vm1Q')
    st.write('Or try [this one](https://www.youtube.com/watch?v=MsWU3VKUduA)')
else:
    st.write('Mini resistance band workout')
    st.video('https://www.youtube.com/watch?v=X2BUjWHPOOo') 

st.divider()

st.header(day + "'s rehab exercises")
st.image('images/guidelines.png', use_column_width="auto")

#    a dictionary of 4 lists: 1. Exercise names; 2. Video URLs showing how to perform the exercises; 3. The exercise summary diagram
database={
    'Exercise name': ["Resisted knee flexion in sitting", "Hamstring curl with exercise band", "Hip extension in standing", "Banded hip extension in standing", "Resisted hip extension in standing", "Single leg RDL", "Single leg bridge", "Bird dog", "Isolated self-myofascial release", "Hamstrings self-myofascial release"],
    'Video':["https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653678&resourceHash=f1388d90eba2f89240103129ef2179b40481c6d4fa81d286de4a1976891cafd6&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653679&resourceHash=b09501893203e932b4ed68d88ef9c113166dfd68cfa59482e93a75feb3ffd410&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653680&resourceHash=c2ebf04d354a35eb677e7a7085339b7958dcd6aed1dc04dbec84ff946709c10e&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653681&resourceHash=5e421365614855170f00a14bd1a7a1862823d40cea9f636abacd5dff8c87218f&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653682&resourceHash=9d0efc6f3ca2cffa7a8a0265eda79fe91cf9cef51beb4395d7e597814ac3d92c&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653683&resourceHash=93ed18c083259690c0ca5f9d4df0f8f9d39cd5808e6f6418c789ff799b9b3b47&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653684&resourceHash=10b7c4a9f4c2b9e0d9c7d5a097685051ee0cf1be6a17bdf9d78a88025fcc44b5&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653685&resourceHash=f6f4b2e2ab2aa4a5bff7827c67e1114e46d7012c16874ab7db2c1335bee370e0&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653686&resourceHash=2b0100bbc1a0284a00bd1b5404ae48fcbda1ef7ef68e67487ae1157a2f3f1003&callerIdentityTag=13146634_745595675", "https://gateway.physiotoolsonline.com/PT_IntegrationService/api/PtSet/GetSetResource?resourceId=20653686&resourceHash=2b0100bbc1a0284a00bd1b5404ae48fcbda1ef7ef68e67487ae1157a2f3f1003&callerIdentityTag=13146634_745595675", ],
    'Instructions':["images/resisted_knee_flexion.png", "images/hamstring_curl.png", "images/hip_extension_standing.png", "images/hip_extension_banded.png", "images/resisted_hip_extension.png", "images/single_leg_rdl.png", "images/single_leg_bridge.png", "images/bird_dog.png", "images/isolated_myofascial_release.png", "images/hamstring_myofascial_release.png"]
}

#   Pass database to pandas dataframe constructor to make 'table'
#   Table has a row for each exercise showing name, video URL and start time in video
table = pd.DataFrame(database)

#table

#   call chose function which picks 6 exercises at random from the table
exercises = choose()
#exercises

#   initialise counter 'number'
number=0

#   Loop through pulling the exercise name from column 1 to put in the Streamlit tab called tab_text
#   then pull the associated video URL from column 2 and set the start time from column 3
for i in exercises:
    number +=1
    tab_text, tab_video = st.tabs(["Exercise " + "%.0f" % number, "Video"])
    with tab_text:
        st.write(f"**{table.iloc[i, 0]}**")
        st.image(table.iloc[i,2], use_column_width="auto")
        st.write("\n")

    with tab_video:
        st.video(table.iloc[i, 1], autoplay=True) 

# block comment of old rehab exercises
#    a dictionary of 3 lists: 1. Exercise names; 2. Video URLs showing how to perform the exercises; 3. The start time in seconds of the relevant bit in the video
#database={
    #'Exercise name': ["Curl up", "Bird dog", "Side plank", "Knee off bed", "Scorpion roll", "SI joint corkscrew", "Windscreen/piriformis rolls", "Tennis ball release", "Donkey kicks", "90\u2070:90\u2070 sacrum lifts", "Wall sits", "Single leg squats", "Clam shells", "Fire hydrants", "Bridges/thrusts/donkey kicks", "Side lying hip abduction", "90\u2070 wall ball roll", "Ball-wall deadlift", "Copenhagens", "Ball squeeze glute bridges", "Banded butterfly bridges", "Reverse lunge step ups"],
    #'Video':["https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=CjinhqRzcaY", "https://www.youtube.com/watch?v=s2bqEP1O6_s", "https://www.youtube.com/watch?v=s2bqEP1O6_s", "https://www.youtube.com/watch?v=Siw3bgdJE80"],
    #'Start time':[68, 295, 205, 58, 323, 446, 603, 71, 524, 169, 377, 686, 474, 490, 505, 524, 279, 397, 0, 430, 334, 111]
#}

#   Pass database to pandas dataframe constructor to make 'table'
#   Table has a row for each exercise showing name, video URL and start time in video
#table = pd.DataFrame(database)

#   table

#   call chose function which picks 6 exercises at random from the table
#exercises = choose()
#   exercises

#   initialise counter 'number'
#number=0

#   Loop through pulling the exercise name from column 1 to put in the Streamlit tab called tab_text
#   then pull the associated video URL from column 2 and set the start time from column 3
#for i in exercises:
    #number +=1
    #tab_text, tab_video = st.tabs(["Exercise " + "%.0f" % number, "Video"])
    #with tab_text:
        #st.write(f"**{table.iloc[i, 0]}**")
        #st.write("\n")

    #with tab_video:
        #st.video(table.iloc[i, 1], start_time=table.iloc[i,2]) 


# block comment of old rehab exercises
#    a dictionary of 3 lists: 1. Exercise names; 2. Video URLs showing how to perform the exercises; 3. The start time in seconds of the relevant bit in the video
#database={
    #'Exercise name': ["Curl up", "Bird dog", "Side plank", "Knee off bed", "Scorpion roll", "SI joint corkscrew", "Windscreen/piriformis rolls", "Tennis ball release", "Donkey kicks", "90\u2070:90\u2070 sacrum lifts", "Wall sits", "Single leg squats", "Clam shells", "Fire hydrants", "Bridges/thrusts/donkey kicks", "Side lying hip abduction", "90\u2070 wall ball roll", "Ball-wall deadlift", "Copenhagens", "Ball squeeze glute bridges", "Banded butterfly bridges", "Reverse lunge step ups"],
    #'Video':["https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=CjinhqRzcaY", "https://www.youtube.com/watch?v=s2bqEP1O6_s", "https://www.youtube.com/watch?v=s2bqEP1O6_s", "https://www.youtube.com/watch?v=Siw3bgdJE80"],
    #'Start time':[68, 295, 205, 58, 323, 446, 603, 71, 524, 169, 377, 686, 474, 490, 505, 524, 279, 397, 0, 430, 334, 111]
#}

#   Pass database to pandas dataframe constructor to make 'table'
#   Table has a row for each exercise showing name, video URL and start time in video
#table = pd.DataFrame(database)

#   table

#   call chose function which picks 6 exercises at random from the table
#exercises = choose()
#   exercises

#   initialise counter 'number'
#number=0

#   Loop through pulling the exercise name from column 1 to put in the Streamlit tab called tab_text
#   then pull the associated video URL from column 2 and set the start time from column 3
#for i in exercises:
    #number +=1
    #tab_text, tab_video = st.tabs(["Exercise " + "%.0f" % number, "Video"])
    #with tab_text:
        #st.write(f"**{table.iloc[i, 0]}**")
        #st.write("\n")

    #with tab_video:
        #st.video(table.iloc[i, 1], start_time=table.iloc[i,2]) 

# block comment of old rehab exercises
#    a dictionary of 3 lists: 1. Exercise names; 2. Video URLs showing how to perform the exercises; 3. The start time in seconds of the relevant bit in the video
#database={
    #'Exercise name': ["Curl up", "Bird dog", "Side plank", "Knee off bed", "Scorpion roll", "SI joint corkscrew", "Windscreen/piriformis rolls", "Tennis ball release", "Donkey kicks", "90\u2070:90\u2070 sacrum lifts", "Wall sits", "Single leg squats", "Clam shells", "Fire hydrants", "Bridges/thrusts/donkey kicks", "Side lying hip abduction", "90\u2070 wall ball roll", "Ball-wall deadlift", "Copenhagens", "Ball squeeze glute bridges", "Banded butterfly bridges", "Reverse lunge step ups"],
    #'Video':["https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=2_e4I-brfqs", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=W8aPYm-CHIk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=7KYfGH8daJk", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=Z-J6rSUpmN4", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=IcmDsB3wdEk", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=Qhk6nrorgT8", "https://www.youtube.com/watch?v=CjinhqRzcaY", "https://www.youtube.com/watch?v=s2bqEP1O6_s", "https://www.youtube.com/watch?v=s2bqEP1O6_s", "https://www.youtube.com/watch?v=Siw3bgdJE80"],
    #'Start time':[68, 295, 205, 58, 323, 446, 603, 71, 524, 169, 377, 686, 474, 490, 505, 524, 279, 397, 0, 430, 334, 111]
#}

#   Pass database to pandas dataframe constructor to make 'table'
#   Table has a row for each exercise showing name, video URL and start time in video
#table = pd.DataFrame(database)

#   table

#   call chose function which picks 6 exercises at random from the table
#exercises = choose()
#   exercises

#   initialise counter 'number'
#number=0

#   Loop through pulling the exercise name from column 1 to put in the Streamlit tab called tab_text
#   then pull the associated video URL from column 2 and set the start time from column 3
#for i in exercises:
    #number +=1
    #tab_text, tab_video = st.tabs(["Exercise " + "%.0f" % number, "Video"])
    #with tab_text:
        #st.write(f"**{table.iloc[i, 0]}**")
        #st.write("\n")

    #with tab_video:
        #st.video(table.iloc[i, 1], start_time=table.iloc[i,2]) 

st.divider()

# Some gym workout schedules and YouTube stretching routines, 1 for each day of the week, to follow.
st.header(day + "'s hamstring exercises")

if day=="Saturday":
    st.image('images/day_1.png')   
elif day=="Sunday":
    st.video("https://www.youtube.com/watch?v=0arLyM00F_w")    
elif day=="Monday":
    st.video('https://www.youtube.com/watch?v=FX-R98zU5MI')
elif day=="Tuesday":
    st.image('images/day_2.png')
elif day=="Wednesday":
    st.video('https://www.youtube.com/watch?v=ui3ToKZtKIs', start_time=30)
elif day=="Thursday":
    st.image('images/day_3.png')
else:
    st.video('https://www.youtube.com/watch?v=FX-R98zU5MI')    

st.divider()

st.header(day + "'s workout")
if day=="Saturday" or day=="Tuesday" or day=="Friday":
    selected = st.radio("Your choice today. What do you feel like doing?", ["I need a rest", "HIIT me", "Pilates ab work", "Hardcore Heria ab work", "Hip, glute & booty workout", "Relaxing yoga", "Step on"], index=None)
    if selected=="I need a rest":
        st.write("OK, see you tomorrow")
    elif selected=="HIIT me" :
        st.video("https://www.youtube.com/watch?v=M0uO8X3_tEA")
        st.write('Lots more like this at  [Juice & Toya\'s YouTube channel](https://www.youtube.com/@JuiceandToya/videos)')
        st.write("It\'s a good channel because she tends to do lower impact modifications while he goes a bit more intense alongside her so you can find a manageable level.")
    elif selected=="Pilates ab work":
        st.video("https://www.youtube.com/watch?v=D6etUH5j2MA")
        st.write("[Move with Nicole](https://www.youtube.com/@MoveWithNicole/videos) is a good channel if you find you like pilates with videos for all body areas")
    elif selected=="Hardcore Heria ab work":
        st.video("https://www.youtube.com/watch?v=XgI_p8bKg78", start_time=71)    
    elif selected == "Hip, glute & booty workout":
        st.video("https://www.youtube.com/watch?v=Pf98VQ0n7jg")
        st.write('Lots more like this on the  [Janekate Fitness YouTube channel](https://www.youtube.com/@JanekateFitness/videos)')
        st.write("Although the focus of this channel is 'bubble butt' looks, the exercises in these videos are great for your 'rear chain' (the hamstrings, glutes and lumbar spine muscles) which fast bowlers need strength in to prevent injuries.")
    elif selected == "Relaxing yoga":
        st.video("https://www.youtube.com/watch?v=ZSSC9X_6wo4", start_time=43)
    elif selected == "Step on":
        st.video("https://www.youtube.com/watch?v=u7c3CtrPKbc")
        st.write('Lots more step workouts like this at  [Get Fit With Rick\'s YouTube channel](https://www.youtube.com/@RickBhullarFitness/videos)')
elif day=="Sunday":
    st.write('20 minutes of calisthenic strength work.')
    st.video("https://www.youtube.com/watch?v=nB0D1a0oC-A")    
elif day=="Monday":
    st.write('20 minutes of full body mobility and stretching.')
    st.video('https://www.youtube.com/watch?v=8fipKUJzcuk')
elif day=="Wednesday":
    st.write('15 minutes of hardcore calisthenic strength work.')
    st.video("https://www.youtube.com/watch?v=gnTzk1yUHB4", start_time=58)
    st.write('If that\'s too much try [this one by Vitality](https://www.youtube.com/watch?v=7PfE9X-TFsY) (with its questionable song lyrics)')
    st.write('Or, even easier, [start with this one](https://www.youtube.com/watch?v=XX1-nL9oM2E) which has 2 identical rounds of exercises. Do just the first round, building up to doing both with time')
else:
    st.write('Relax. Breathe deep, get into your own head and feel your chakras. 20 minutes of yoga.')
    st.video('https://www.youtube.com/watch?v=b1H3xO3x_Js')
    st.write('Lots more like this at  [Adriene\'s YouTube channel](https://www.youtube.com/@yogawithadriene/videos)')