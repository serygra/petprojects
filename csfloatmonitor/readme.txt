CSFloat Emailer

This is an emailer utilizing the csfloat api to notify me when there are price drops below a certain threshold for an item that I wanted to purchase. 
I run this as a cronjob on my PC, if you're interested in doing this Tony Teaches Tech has an awesome tutorial on YouTube (How to Schedule a Python Script with a Cron Job. 

THINGS TO NOTE:
1) The sendemailscript file is set up to work with a GMAIL account (line 14).
2) Look for "modification required" comments to get this to work on your own setup.
3) To figure out the def_index and paint_index all you need to do is search your desired item in csfloat and it's visible in your URL.

FUTURE UPDATES:
Will try to append spammy results into an empty list to avoid them from being thrown all day. If alerts get too repetitive you can always remove your API key in CSFloat settings to stop.

Will try to add better params (i.e., iteratively taking item name and item type and converting to the indexes), but since this isn't natively available in the API I'll need to either:
1) manually hard code all item types and item names in a massive dictionary (not great).
2) figure out a way to use the curl response to map def_index and paint_index to item description (I'm a beginner so this is going to take me a bit to figure out).

Once I can figure this out then I will likely set up a GUI to configure search values instead of editing the raw .py file.
