from flask import Flask, jsonify
from podcasts import podcasts
import json

app = Flask(__name__)

#The 3 next routes are focused On reading and filtering the JSON
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


#The next route will help us to create a file with the top 20 podcasts
@app.route('/podcaststop20') 
def getPodcastsTop20():
    podcaststop20 = [podcast for podcast in  podcasts] #with this line all the JSON is read
    pod = 0
    data = ''

    if (len(podcaststop20) > 0): # The JSON is validated to have information
        while pod <= 19: # the top 20 podcasts are read and saved in the variable data
            data = data + str(podcaststop20[pod])
            pod = pod + 1
    
    with open('podcastTop20.json', 'w') as json_file: # The new JSON with the top 20 is created
        json.dump(data, json_file, indent=4)
    
    return jsonify({"message":"Top 20 Podcasts were created successfully in podcastTop20.json. Please, verify on your main folder"})

    
   
       # return jsonify({"podcast": podcaststop20})
    
    # podcaststop20 = jsonify(podcasts)
    # with open('podcastsTop20.json', 'w') as json_file:
    #     json.dump(podcaststop20, json_file)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
