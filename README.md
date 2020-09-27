# Liked Videos Search for TikTok

## Inspiration
We are users of the popular mobile app, TikTok. One frustration we continued running into time and time again with using TikTok is the fact that there was no easy way to search through your liked videos in order to show a TikTok you once saw, to a friend. The only way to search through liked videos in the official app is to scroll down through the list of every single video you have ever liked in chronological order. This is time-consuming, tedious, and inefficient.

## What it does
Our app allows a user to enter a username and a search query, and returns a list of TikToks in that user's most recent (1000) liked videos that match their search query.

## How we built it
We found and used the Unofficial TikTok API In Python, which allowed us to find a list of any given user's most recent (1000) liked videos, considering that they had their privacy settings on public. We then looped through the list, searching for any TikTok containing the search query in either the description, author's id, author's name, sound title, or sound author and returned a link to every match.

## Challenges we ran into
We were very busy throughout the weekend with homework for classes, so we were not able to put as much time into the project as we had hoped. We also ran into some issues with setting up a virtualenv, getting the TikTokAPI to work, and figuring out how to search through the Python TikTok dictionaries.

## Accomplishments that we're proud of
Besides the obstacles we faced, we are still proud of how fast we were able to get a minimum viable product up and running. And we are proud of our idea, seeing more future development and more time being put in to it coming soon. We can't wait to share this tool with many of our friends who may find it to be very useful.

## What we learned
Neither of us had ever used the Unofficial TikTokAPI and we learned how to use it specifically for this project.

## What's next for Liked Videos Search for TikTok
We would like to make it more presentable and user friendly, by instead of just returning a list of links to all the TikToks, we host the tool on a website and return dynamic images to the user, similar to how it would look on the TikTok app. We would also like to optimize our search algorithm, which we had ideas on how to do, but did not have time to implement during the hackathon.
