#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlib


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


# Membaca data dari spreadsheet
url = 'https://docs.google.com/spreadsheets/d/1ZGAr4vhY2YLcl5x7yf81tVdxGyKT5bCmtmCwijZfe4E/export?format=csv&gid=739468979'
data = pd.read_csv(url)


# In[4]:


data


# In[5]:


# Visualisasi Diagram Batang: Jumlah Gol Tim Tuan Rumah dan Tim Tamu
home_goals = data['Home Team Goals'].sum()
away_goals = data['Away Team Goals'].sum()

plt.bar(['Tim Tuan Rumah', 'Tim Tamu'], [home_goals, away_goals])
plt.title('Total Jumlah Gol')
plt.xlabel('Tim')
plt.ylabel('Jumlah Gol')
plt.show()


# In[6]:


#Persentase Kemenangan Berdasarkan Win Conditions
win_conditions = data['Win conditions'].value_counts()
labels = win_conditions.index
sizes = win_conditions.values

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Persentase Kemenangan Berdasarkan Win Conditions')
plt.axis('equal')
plt.show()


# In[7]:


# Visualisasi Histogram: Attendance keep
attendance = data['Attendance']

plt.hist(attendance, bins=10)
plt.title('Distribusi Attendance')
plt.xlabel('Attendance')
plt.ylabel('Frekuensi')
plt.show()


# In[8]:


#keep
goals = pd.concat([data['Home Team Goals'], data['Away Team Goals']])

plt.boxplot(goals)
plt.title('Distribusi Jumlah Gol')
plt.ylabel('Jumlah Gol')
plt.show()


# In[9]:


home_goals_stadium = data.groupby('Stadium')['Home Team Goals'].sum()

plt.bar(home_goals_stadium.index, home_goals_stadium.values)
plt.title('Jumlah Gol Tim Tuan Rumah per Stadium')
plt.xlabel('Stadium')
plt.ylabel('Jumlah Gol')
plt.xticks(rotation=90)
plt.show()


# In[10]:


#Perbandingan persentase kemenangan Home Team dan Away Team
home_wins = len(data[data['Home Team Goals'] > data['Away Team Goals']])
away_wins = len(data[data['Home Team Goals'] < data['Away Team Goals']])

plt.pie([home_wins, away_wins], labels=['Tim Tuan Rumah', 'Tim Tamu'], autopct='%1.1f%%')
plt.title('Persentase Kemenangan Tim Tuan Rumah dan Tim Tamu')
plt.axis('equal')
plt.show()


# In[11]:


attendance_stadium = data.groupby('Stadium')['Attendance'].mean()

plt.scatter(attendance_stadium.index, attendance_stadium.values)
plt.title('Distribusi Jumlah Penonton berdasarkan Stadium')
plt.xlabel('Stadium')
plt.ylabel('Jumlah Penonton')
plt.xticks(rotation=90)
plt.show()


# In[12]:


home_goals_time = data.groupby('Datetime')['Home Team Goals'].sum()
away_goals_time = data.groupby('Datetime')['Away Team Goals'].sum()

plt.plot(home_goals_time.index, home_goals_time.values, label='Tim Tuan Rumah')
plt.plot(away_goals_time.index, away_goals_time.values, label='Tim Tamu')
plt.title('Jumlah Gol Tim Tuan Rumah dan Tim Tamu dari Waktu ke Waktu')
plt.xlabel('Waktu')
plt.ylabel('Jumlah Gol')
plt.legend()
plt.xticks(rotation=45)
plt.show()


# In[13]:


home_attendance = data.groupby('Home Team Name')['Attendance'].mean()
away_attendance = data.groupby('Away Team Name')['Attendance'].mean()

plt.boxplot([home_attendance, away_attendance], labels=['Tim Tuan Rumah', 'Tim Tamu'])
plt.title('Distribusi Kehadiran Penonton berdasarkan Tim')
plt.ylabel('Kehadiran Penonton')
plt.show()


# In[4]:


half_time_home_goals = data['Half-time Home Goals'].sum()
half_time_away_goals = data['Half-time Away Goals'].sum()

plt.bar(['Home Team', 'Away Team'], [half_time_home_goals, half_time_away_goals])
plt.title('Jumlah Gol Babak Paruh Pertama')
plt.xlabel('Babak Paruh Pertama')
plt.ylabel('Jumlah Gol')
plt.show()


# In[15]:


home_wins = len(data[data['Home Team Goals'] > data['Away Team Goals']])
away_wins = len(data[data['Home Team Goals'] < data['Away Team Goals']])
draws = len(data[data['Home Team Goals'] == data['Away Team Goals']])

plt.pie([home_wins, away_wins, draws], labels=['Tim Tuan Rumah', 'Tim Tamu', 'Draw'], autopct='%1.1f%%')
plt.title('Persentase Kemenangan Tim Tuan Rumah dan Tim Tamu')
plt.axis('equal')
plt.show()


# In[16]:


attendance_city = data.groupby('City')['Attendance'].mean()

plt.scatter(attendance_city.index, attendance_city.values)
plt.title('Distribusi Jumlah Penonton berdasarkan Kota')
plt.xlabel('Kota')
plt.ylabel('Jumlah Penonton')
plt.xticks(rotation=90)
plt.show()


# In[17]:


half_time_home_goals_time = data.groupby('Datetime')['Half-time Home Goals'].sum()
half_time_away_goals_time = data.groupby('Datetime')['Half-time Away Goals'].sum()

plt.plot(half_time_home_goals_time.index, half_time_home_goals_time.values, label='Babak Pertama')
plt.plot(half_time_away_goals_time.index, half_time_away_goals_time.values, label='Babak Kedua')
plt.title('Jumlah Gol per Babak dari Waktu ke Waktu')
plt.xlabel('Waktu')
plt.ylabel('Jumlah Gol')
plt.legend()
plt.xticks(rotation=45)
plt.show()


# In[18]:


#keep
attendance_stadium = data.groupby('Stadium')['Attendance'].mean()

plt.boxplot(attendance_stadium.values)
plt.title('Distribusi Kehadiran Penonton berdasarkan Stadion')
plt.ylabel('Kehadiran Penonton')
plt.xticks([1], ['Stadion'])
plt.show()


# In[19]:


#Top 10 Jumlah Gol Terbanyak oleh Wasit
referee_goals = data.groupby('Referee')['Home Team Goals'].sum() + data.groupby('Referee')['Away Team Goals'].sum()
referee_goals = referee_goals.sort_values(ascending=False).head(10)

plt.bar(referee_goals.index, referee_goals.values)
plt.title('Jumlah Gol per Wasit')
plt.xlabel('Wasit')
plt.ylabel('Jumlah Gol')
plt.xticks(rotation=90)
plt.show()


# In[20]:


home_wins = len(data[data['Home Team Goals'] > data['Away Team Goals']])
away_wins = len(data[data['Home Team Goals'] < data['Away Team Goals']])
draws = len(data[data['Home Team Goals'] == data['Away Team Goals']])

plt.pie([home_wins, away_wins, draws], labels=['Tim Tuan Rumah', 'Tim Tamu', 'Draw'], autopct='%1.1f%%')
plt.title('Persentase Kemenangan Tim Tuan Rumah, Tim Tamu, dan Draw')
plt.axis('equal')
plt.show()


# In[21]:


attendance_home_team = data.groupby('Home Team Name')['Attendance'].mean()
attendance_away_team = data.groupby('Away Team Name')['Attendance'].mean()

plt.scatter(attendance_home_team.index, attendance_home_team.values, label='Tim Tuan Rumah')
plt.scatter(attendance_away_team.index, attendance_away_team.values, label='Tim Tamu')
plt.title('Distribusi Jumlah Penonton berdasarkan Tim')
plt.xlabel('Tim')
plt.ylabel('Jumlah Penonton')
plt.xticks(rotation=90)
plt.legend()
plt.show()


# In[22]:


referee_goals_time = data.groupby('Datetime')['Home Team Goals'].sum() + data.groupby('Datetime')['Away Team Goals'].sum()

plt.plot(referee_goals_time.index, referee_goals_time.values)
plt.title('Jumlah Gol per Wasit dari Waktu ke Waktu')
plt.xlabel('Waktu')
plt.ylabel('Jumlah Gol')
plt.xticks(rotation=45)
plt.show()


# In[23]:


#Distribusi jumlah Gol per Stadium tiap Tim
home_team_goals_stadium = data.groupby('Stadium')['Home Team Goals'].sum()
away_team_goals_stadium = data.groupby('Stadium')['Away Team Goals'].sum()

plt.boxplot([home_team_goals_stadium, away_team_goals_stadium], labels=['Tim Tuan Rumah', 'Tim Tamu'])
plt.title('Distribusi Jumlah Gol per Stadium')
plt.ylabel('Jumlah Gol')
plt.xticks([1, 2], ['Tim Tuan Rumah', 'Tim Tamu'])
plt.show()


# In[24]:


plt.scatter(data['Home Team Goals'], data['Attendance'])
plt.title('Hubungan antara Jumlah Gol Tim Tuan Rumah dan Kehadiran Penonton')
plt.xlabel('Jumlah Gol Tim Tuan Rumah')
plt.ylabel('Kehadiran Penonton')
plt.show()


# In[26]:


#keep
matches_per_year = data.groupby('Year')['MatchID'].nunique()

plt.bar(matches_per_year.index, matches_per_year.values)
plt.title('Jumlah Pertandingan per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Pertandingan')
plt.xticks(rotation=45)
plt.show()


# In[28]:


goals_per_year = data.groupby('Year')['Home Team Goals'].sum() + data.groupby('Year')['Away Team Goals'].sum()

plt.plot(goals_per_year.index, goals_per_year.values)
plt.title('Jumlah Gol per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Gol')
plt.xticks(rotation=45)
plt.show()


# In[32]:


matches_per_stadium = data.groupby('Stadium')['MatchID'].nunique().nlargest(10)

plt.bar(matches_per_stadium.index, matches_per_stadium.values)
plt.title('Number of Matches per Stadium')
plt.xlabel('Stadium')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


# In[33]:


plt.hist(data['Home Team Goals'], bins=10)
plt.title('Distribution of Home Team Goals')
plt.xlabel('Goals')
plt.ylabel('Frequency')
plt.show()


# In[34]:


average_attendance_per_year = data.groupby('Year')['Attendance'].mean()

plt.plot(average_attendance_per_year.index, average_attendance_per_year.values)
plt.title('Average Attendance per Year')
plt.xlabel('Year')
plt.ylabel('Average Attendance')
plt.xticks(rotation=45)
plt.show()


# In[35]:


plt.scatter(data['Half-time Home Goals'], data['Half-time Away Goals'])
plt.title('Relationship between Half-time Home Goals and Half-time Away Goals')
plt.xlabel('Half-time Home Goals')
plt.ylabel('Half-time Away Goals')
plt.show()


# In[36]:


win_count_home_initials = data[data['Home Team Goals'] > data['Away Team Goals']]['Home Team Initials'].value_counts()

plt.pie(win_count_home_initials.values, labels=win_count_home_initials.index, autopct='%1.1f%%')
plt.title('Win Distribution by Home Team Initials')
plt.axis('equal')
plt.show()


# In[37]:


top_referees = data['Referee'].value_counts().nlargest(10)

plt.bar(top_referees.index, top_referees.values)
plt.title('Top 10 Referees with the Most Matches')
plt.xlabel('Referee')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


# In[2]:


matches_over_time = data.groupby('Year')['MatchID'].nunique()

plt.plot(matches_over_time.index, matches_over_time.values)
plt.title('Jumlah Pertandingan dari Waktu ke Waktu')
plt.xlabel('Year')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


# In[40]:


away_goals_round = [data[data['RoundID'] == round_id]['Away Team Goals'] for round_id in data['RoundID'].unique()]

plt.boxplot(away_goals_round, labels=data['RoundID'].unique())
plt.title('Distribution of Away Team Goals by RoundID')
plt.xlabel('RoundID')
plt.ylabel('Away Team Goals')
plt.show()


# In[41]:


plt.scatter(data['Home Team Goals'], data['Away Team Goals'])
plt.title('Relationship between Home Team Goals and Away Team Goals')
plt.xlabel('Home Team Goals')
plt.ylabel('Away Team Goals')
plt.show()


# In[42]:


plt.hist(data['Attendance'], bins=10)
plt.title('Distribution of Attendance')
plt.xlabel('Attendance')
plt.ylabel('Frequency')
plt.show()


# In[43]:


average_home_goals_per_year = data.groupby('Year')['Home Team Goals'].mean()

plt.plot(average_home_goals_per_year.index, average_home_goals_per_year.values)
plt.title('Average Home Team Goals per Year')
plt.xlabel('Year')
plt.ylabel('Average Home Team Goals')
plt.xticks(rotation=45)
plt.show()


# In[44]:


matches_per_city = data.groupby('City')['MatchID'].nunique().nlargest(10)

plt.bar(matches_per_city.index, matches_per_city.values)
plt.title('Number of Matches per City')
plt.xlabel('City')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


# In[45]:


home_goals_stage = [data[data['Stage'] == stage]['Home Team Goals'] for stage in data['Stage'].unique()]

plt.boxplot(home_goals_stage, labels=data['Stage'].unique())
plt.title('Distribution of Home Team Goals by Stage')
plt.xlabel('Stage')
plt.ylabel('Home Team Goals')
plt.show()


# In[46]:


win_count_away_initials = data[data['Home Team Goals'] < data['Away Team Goals']]['Away Team Initials'].value_counts()

plt.pie(win_count_away_initials.values, labels=win_count_away_initials.index, autopct='%1.1f%%')
plt.title('Win Distribution by Away Team Initials')
plt.axis('equal')
plt.show()


# In[47]:


matches_per_home_team = data.groupby('Home Team Name')['MatchID'].nunique().nlargest(10)

plt.plot(matches_per_home_team.index, matches_per_home_team.values)
plt.title('Number of Matches per Home Team')
plt.xlabel('Home Team')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


# In[49]:


plt.scatter(data['Attendance'], data['Home Team Goals'] + data['Away Team Goals'])
plt.title('Relationship between Attendance and Number of Goals')
plt.xlabel('Attendance')
plt.ylabel('Number of Goals')
plt.show()


# In[50]:


average_away_goals_per_year = data.groupby('Year')['Away Team Goals'].mean()

plt.plot(average_away_goals_per_year.index, average_away_goals_per_year.values)
plt.title('Average Away Team Goals per Year')
plt.xlabel('Year')
plt.ylabel('Average Away Team Goals')
plt.xticks(rotation=45)
plt.show()


# In[52]:


home_goals_stage = [data[data['Stage'] == stage]['Home Team Goals'] for stage in data['Stage'].unique()]

plt.boxplot(home_goals_stage, labels=data['Stage'].unique())
plt.title('Distribution of Home Team Goals by Stage')
plt.xlabel('Stage')
plt.ylabel('Home Team Goals')
plt.show()


# In[53]:


win_count_home_initials = data[data['Home Team Goals'] > data['Away Team Goals']]['Home Team Initials'].value_counts()

plt.pie(win_count_home_initials.values, labels=win_count_home_initials.index, autopct='%1.1f%%')
plt.title('Win Distribution by Home Team Initials')
plt.axis('equal')
plt.show()


# In[54]:


matches_per_city = data.groupby('City')['MatchID'].nunique().nlargest(10)

plt.bar(matches_per_city.index, matches_per_city.values)
plt.title('Number of Matches per City')
plt.xlabel('City')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


# In[55]:


average_attendance_per_year = data.groupby('Year')['Attendance'].mean()

plt.plot(average_attendance_per_year.index, average_attendance_per_year.values)
plt.title('Average Attendance per Year')
plt.xlabel('Year')
plt.ylabel('Average Attendance')
plt.xticks(rotation=45)
plt.show()


# In[56]:


plt.scatter(data['Half-time Home Goals'], data['Half-time Away Goals'])
plt.title('Relationship between Half-time Home Goals and Half-time Away Goals')
plt.xlabel('Half-time Home Goals')
plt.ylabel('Half-time Away Goals')
plt.show()


# In[57]:


plt.hist(data['Home Team Goals'], bins=10)
plt.title('Distribution of Home Team Goals')
plt.xlabel('Home Team Goals')
plt.ylabel('Frequency')
plt.show()


# In[58]:


matches_per_year = data.groupby('Year')['MatchID'].nunique()

plt.plot(matches_per_year.index, matches_per_year.values)
plt.title('Number of Matches per Year')
plt.xlabel('Year')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


# In[59]:


matches_per_stadium = data.groupby('Stadium')['MatchID'].nunique().nlargest(10)

plt.bar(matches_per_stadium.index, matches_per_stadium.values)
plt.title('Number of Matches per Stadium')
plt.xlabel('Stadium')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




