---
title: "Making a Movie"
parent: Map Viewer
grand_parent: Graphical Interface
nav_order: 6
---
{% raw %}
# Making a Movie

The Map Viewer generates [mp4](https://en.wikipedia.org/wiki/MPEG-4_Part_14) movies from a set of maps. This is useful because:

- Movies display temporal changes in presentations.
- Any device or application that supports mp4 can play the movie; it does not depend on map formats or on Dinamica EGO.
- The generated frames can be saved separately as PNG files, for use in other movie creation tools.

## How Movies Are Built

A movie is a series of frames displayed at a given time interval. In the Map Viewer, the loaded maps are the frames: configure the main viewer area as it should appear in the movie. Zoom, pan, histogram curves, the palette of each map, and transparency are kept in the movie.

## Steps

1. Load the maps to display. See [Loading Maps](Map-Viewer-Interface.html#loading-maps).
2. Configure the transformations, [histogram](Histogram-Editor.html) curves, and [color palette](Color-Palette.html).
3. Open the movie maker.

   ![Movie maker button](../image/movie_maker_button.png)

4. In the wizard, select the frames to be replaced (left column) and the frames that replace them after each frame (right column).

   ![Selecting frames](../image/movie_1.png)

5. Set the time between frames. A preview shows the replacement speed.

   ![Time between frames](../image/movie_2.png)

6. Select the path of the output mp4 file and whether to keep the generated frames.

   ![Output path](../image/movie_3.png)

7. Click Next and wait while the movie is generated.

   ![Generating the movie](../image/movie_4.png)

   The frame names in the Map column of the main window show the progress. A notification appears when the process finishes.

   ![Movie finished](../image/movie_5.png)
{% endraw %}
