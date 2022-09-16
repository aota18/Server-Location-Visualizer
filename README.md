# Server-Location-Visualizer

![Screenshot](./screenshot.png)

This is a Server Location Visualizer project with python & javascript (Google Map API).

You can see the locations of the server that I've visited for a month and its detail in the map.

Try out the quick [Demo](https://server-location-visualizer-gg4nzrntd-aota18.vercel.app/) before the description.

This project is a implementation of this project idea. (https://practicalpython.yasoob.me/chapter9.html#)

---

## Data sourcing and preprocessing

You can export the history of your website you've visited from Chrome browser.(I used this [chrome extension](https://chrome.google.com/webstore/detail/export-chrome-history/dihloblpkeiddiaojbagoecedbfpifdj/related?hl=en) for export).

With above extension, You can get the list of websites you've visited from chrome history. I selected a date from today to month ago.

```
https://nomad-wannabe.tistory.com/50
https://jikimdiary.tistory.com/10
...

```

In `history.txt`, There are thousands of lists that you've exported from extension and I did some cleaning task before I pass them to the API. (Filtering duplicates and only leave the domain address.)

---

## API Info

You can use ipinfo (https://ipinfo.io) for converting domain names to IP detail.

---

## Visualization

I used [Google Map APIs](https://developers.google.com/maps) for the marker and tooltips for this project.
