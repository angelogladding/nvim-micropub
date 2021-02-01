"""Use nvim as a Micropub editor."""

import pynvim
import requests


@pynvim.plugin
class Micropub:
    """The nvim <-> Micropub bridge."""

    def __init__(self, vim):
        self.vim = vim
        self.micropub_endpoint = self.vim.vars["indieweb_micropub_endpoint"]
        self.access_token = self.vim.vars["indieweb_access_token"]
        self.headers = {"Authorization": f"Bearer {self.access_token}"}

    @pynvim.autocmd("BufReadCmd", pattern="site:*.md",
                    eval="expand('<afile>')", sync=True)
    def read_handler(self, filename):
        entry = requests.get(f"{self.micropub_endpoint}?q=source&"
                             f"url=/{filename}", headers=self.headers)
        self.vim.current.buffer[0] = entry.text

    @pynvim.autocmd("BufWriteCmd", pattern="site:*.md",
                    eval="expand('<afile>')", sync=True)
    def write_handler(self, filename):
        entry = {"type": ["h-entry"],
                 "properties": {"content": "\n".join(self.vim.current.buffer)}}
        response = requests.post(self.micropub_endpoint, json=entry,
                                 headers=self.headers)
        if response.ok:
            self.vim.out_write("Published!\n")
        else:
            self.vim.err_write("Couldn't publish!\n")
