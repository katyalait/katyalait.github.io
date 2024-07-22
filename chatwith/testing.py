import json

with open("data/dataset.json") as f:
	posts = json.load(f)

user_data = {}

lines_ignored = 0
for post in posts:
	if 'ownerUsername' not in post:
		lines_ignored += 1
	else:
		username = post['ownerUsername']
		if username not in user_data:
			user_data[username] = []
		user_data[username].append(post)

post_count = {username: len(posts) for username, posts in user_data.items()}


print(json.dumps(post_count, indent=4))
print(f"Lines ignored: {lines_ignored}")