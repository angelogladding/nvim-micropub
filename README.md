# nvim-micropub
use nvim as a Micropub editor

## Install

Copy `nvim-micropub.py` to `~/.config/nvim/rplugin/python3/` and execute `UpdateRemotePlugins` from within nvim.

Add to your `~/.config/nvim/init.vim`:

    let g:indieweb_micropub_endpoint='https://example.com/micropub';
    let g:indieweb_access_token='XKJHA...';

## Use

    $ nvim site:pagename.md

The file will be read using `q=source` and written to using a Micropub create or update.
