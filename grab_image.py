import requests

image = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/World_Chess_Championship_1985_USSR_stamp.jpg/260px-World_Chess_Championship_1985_USSR_stamp.jpg")

# write in binary
f = open ("my_image.jpg","wb")
f.write(image.content)
f.close()