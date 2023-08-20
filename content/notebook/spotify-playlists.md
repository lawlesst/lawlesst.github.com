Title:Creating Spotify Playlists via the Spotify API
Date:08-20-2023
Slug:spotify-playlists

I've recently pushed [code](https://github.com/lawlesst/spotify-playlists) to Github for a little hobby project I've been working. There are public radio music shows that I enjoy but am often not able to listen to because they are aired at a time that I'm busy. It's more convenient to listen on demand. I also spend most of my listening time in the Spotify app so I would rather listen there even if the show offers a feed from their site, and many don't. 

While exploring the possibility of creating Spotify playlists of these shows, I learned that many of them publish their playlists on their show sites using an undocumented API provided by National Public Radio. I was able to use my browser to determine what HTTP calls I need to make to get the latest episodes and the tracks played. I was then able (after a rather steep learning curve) use the [Spotify API](https://developer.spotify.com/documentation/web-api) to create playlists for the shows I'm interested in. 

Now I'm able to run a script that will harvest the playlists for shows I'm interested in and update Spotify playlists that I can listen to at my convenience. I miss the DJ's introduction to songs and any local flavor of the show but it allows me to hear the music on demand. As I listen, the tracks become part of my Spotify listening history that can be mined by Spotify to offer me additional recommendations. 

Since there were a few technical hurdles, mostly around authentication, with the Spotify API, I posted my [code](https://github.com/lawlesst/spotify-playlists) for others to review. I may post more in-depth about this later. The [project README](https://github.com/lawlesst/spotify-playlists) also includes more details on how to get started with the Spotify API.

Here are some of the shows I'm harvesting and their corresponding public Spotify playlist that I've created. You should still donate to your favorite public radio station. 

* [WEMU Roots Music Project with Jeremy Baldwin](https://www.wemu.org/show/the-roots-music-project-with-jeremy-baldwin) - [playlist](https://open.spotify.com/playlist/5CL6kh3r9obk4N7T5wPwnt?si=34bc11c915ac4655)
* [HPPR: High Plains Morning](https://www.hppr.org/show/high-plains-morning) - [playlist](https://open.spotify.com/playlist/7iVnCseOptNviUNe8nRPGp?si=12c7c9fcfee1475a)
* [WNCW: Cosmic American Music Show](https://www.wncw.org/show/cosmic-american-music-show) - [playlist](https://open.spotify.com/playlist/4y3IOtVq0MSGODMZMNQuuE?si=fed2f69a703e45fe)