# Server-Location-Visualizer

Server Location Visualizer project with python & D3.JS

[-] Sourcing the data - export the history from browser (I used chrome extension : https://chrome.google.com/webstore/detail/export-chrome-history/dihloblpkeiddiaojbagoecedbfpifdj/related?hl=en)

[-] Cleaning the data

    ```
    https://google.com/abc
    https://google.com/what..
    ```
    [-] because we don't want duplicate server, we have to filter the urls out and only keep the unique URL.

[-] Domain name to IP address

    ```

    $ ping pythonbasics.org

    PING pythonbasics.org (172.67.195.177): 56 data bytes
    64 bytes from 172.67.195.177: icmp_seq=0 ttl=57 time=5.016 ms
    ...

    ```

    - If you ping 'domain', you can get the address of its domain.

[-] Get IP detail using ipinfo (https://ipinfo.io)

    - create account and get token
    - (option) boost up the speed of getting result using multi-threading

[-] Visualization

    - Used D3 bubble map library to show the map chart. (https://d3-graph-gallery.com/graph/bubblemap_tooltip.html)
    - When user mouseup on the bubble, It shows the detail like domain, ip, country, city , lat&lon data.
