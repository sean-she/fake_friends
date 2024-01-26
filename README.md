# Instagram Fake Freinds Finder

### Author: Sean She

This script will output profile links to all the people who aren't following you back on Instagram as well as the number of following and followers.

***

## How do I get my followers/following data?

1. Go to this Instagram [link](https://www.instagram.com/download/request) to request your data.
2. Select "JSON" for the Information format section.
3. Your data should come within a few hours, even though Instagram says it may take longer.

***

## Setting up the script

1.  Once you receive your data, unzip the folder and navigate to `followers_and_following`.
2. Your followers/following data should be the last two files in the `followers_and_following` folder, but if not, you can look at the name of the files to confirm which ones you need.
3. Drag the two files into the repo and appropriately rename them to be `followers` and `following`.
4. Open up a terminal and cd into the repo
5. Run `python3 fakefriends.py`
6. Unfollow these fake friends!
