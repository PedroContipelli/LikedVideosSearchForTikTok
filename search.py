from TikTokApi import TikTokApi
api = TikTokApi()

username = input('Enter your username: ')
print('Searching in @' + username + '\'s liked videos...')

num_videos = 1000

user = api.user(username=username)
liked_vids = user.liked(count=num_videos)

search_query = input('Search: ').lower()

for tiktok in liked_vids:
	search_values = [tiktok['desc'], tiktok['author']['uniqueId'], tiktok['author']['nickname'], tiktok['music']['title'], tiktok['music']['authorName']]
	search_values = [str.lower() for str in search_values]

	for search_val in search_values:
		if search_query in search_val:
			URL = 'https://www.tiktok.com/@' + tiktok['author']['uniqueId'] + '/video/' + tiktok['id']
			print(URL)
			break

# End
