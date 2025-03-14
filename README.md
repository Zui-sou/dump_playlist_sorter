# Dump Playlist sorter

Uses the Spotify API to scrape and sort a given playlist using [Oil.nvim](https://github.com/stevearc/oil.nvim). Is it practical, not at all, but it was a fun project for me to learn API things and general Python knowledge.

## Usage

If for some reason you want to use this abomination, here are the steps you need to take:

### Setup

- A [SpotifyAPI](https://developer.spotify.com/) key.
    * Login and create an app.
    * Copy the Secret and Client id's and put them into a .env file in the base root of the project like this
        + `CLIENT_ID="xxx"` 
        + `SECRET_ID="xxx"`
- Neovim with the [Oil.nvim](https://github.com/stevearc/oil.nvim) plugin installed
    * There are tutorials everywhere for Nvim plugins but my favorite is [this](https://www.youtube.com/watch?v=zHTeCSVAFNY) one by [typecraft](https://www.youtube.com/@typecraft_dev)
        + The only caveat is that in the `oil.setup()` make sure you add `default_file_explorer = true` so it should look something like this `oil.setup({ default_file_explorer = true })`
        + NOTE: I only use [lazy.nvim](https://github.com/folke/lazy.nvim) as my package manager so I'm not sure how exactly the setup function works with different pacage managers

### Actual Usage

Once the above steps are taken, make a venv, install requirements.txt, run `main.py` and everything should work. 
> [!NOTE]
> The first run might take a tad longer because it has to make a refresh token.


## Todo

- [ ] Make get_refresh_token function in auth.py
- [ ] Scrape Dump Playlist
- [ ] Make folder with all songs from said playlist
- [ ] Read sorted songs
- [ ] Add sorted songs to new playlists
- [ ] Clear dump playlist
