# FocusSV
Python Backend Developer Test

Resolution of first exercise: A service to provide a search lookup within the podcasts.
  1. Create a folder with the name that you prefer, in this case was named Python_Exercise
  2. Inside the folder you most to copy the next files. 
      podcast.py which contains the JSON.
      app.py which contains the routes with their different filters by podcast name and podcast artist name, also contains the configuration of Server's port.
  3. Using the framework of your preference, you can visualize both files. In this case, Visual Studio Code was used.
  4. Using the terminal you write the next instruction: python app.py
  5. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcasts/Nice%20White%20Parents to filter by podcast name
  5. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcastsname/The%20New%20York%20Times to filter by podcast artist name

Resolution of second exercise: A service that would allow to save the top 20 podcasts to a separate JSON File
  1. The file app.py was modified, it was added the route '/podcaststop20'
  2. Using the framework of your preference, you can visualize the file. In this case, Visual Studio Code was used.
  3. Using the terminal you write the next instruction: python app.py
  4. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcaststop20 
  5. Once the process finished, the file podcastTop20.json is created in the main folder.
 
Resolution of third exercise: A service to replace the top 20 podcasts for the bottom 20 to said JSON File
  1. The file app.py was modified, it was added the route '/podcastsbottom20'
  2. Using the framework of your preference, you can visualize the file. In this case, Visual Studio Code was used.
  3. Using the terminal you write the next instruction: python app.py
  4. Open your preferred browser and write in the url bar the next example url http://localhost:5000/podcastsbottom20
  5. Once the process finished, the file 20podcasts.json is updated in the main folder.
