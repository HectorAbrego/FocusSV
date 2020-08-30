from flask import Flask, jsonify
from podcasts import podcasts

app = Flask(__name__)

# If you want to see the all podcasts
@app.route('/podcasts') 
def getPodcasts():
    return jsonify({"podcasts": podcasts, "message": "Product's List"})

# If you want to filter the podcasts by name
@app.route('/podcasts/<string:podcast_name>') 
def getPodcast(podcast_name):
    podcastFound = [podcast for podcast in  podcasts if podcast['name'] == podcast_name]
    if (len(podcastFound) > 0):
        return jsonify({"podcast": podcastFound})
    return jsonify({"message":"Podcast not found"})

# If you want to filter the podcasts by artist name
@app.route('/podcastsname/<string:podcast_artistName>') 
def getPodcastName(podcast_artistName):
    podcastFound = [podcast for podcast in  podcasts if podcast['artistName'] == podcast_artistName]
    if (len(podcastFound) > 0):
        return jsonify({"podcast": podcastFound})
    return jsonify({"message":"Podcast not found"})
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
