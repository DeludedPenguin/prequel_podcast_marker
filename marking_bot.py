
# user inputs podcast mark and sko mark, save as variables

print('Please enter Podcast Mark (out of 100): ')
podcast_mark = float(input())

print('Please enter SKO Mark (out of 100): ')
sko_mark = float(input())

# portion of podcast mark saved as 3/4 of AT4
podcast_portion = (podcast_mark/100)*75

# calculate portion of SKO mark saved as 1/4 of AT4
sko_portion = (sko_mark/100)*25

# calculate AT4 mark as percentage
at4_mark = podcast_portion + sko_portion

# change variable to offer AT5.2 mark as percentage
at5_2mark = sko_mark

# calculate final AT4 and AT5.2 grades as rounded numbers with weightings
at4_final = round(at4_mark*0.4)
at5_2final = round(at5_2mark*0.15)

# print all outputs
print('Assessment Task 4 mark is: ',at4_mark)
print('Assessment Task 5.2 mark is: ',at5_2mark)
print('Final grade for AT4 (out of 40) is: ',at4_final)
print('Final grade for AT5.2 (out of 15) is: ',at5_2final)
