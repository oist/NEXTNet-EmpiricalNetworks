# Collection of empirical networks

This repository contains a collection of empirical networks from the SNAP (Leskovec and Krevl, [2014](http://snap.stanford.edu/data)), ICON (Clauset *et al.*, [2016](https://icon.colorado.edu/)) and KONECT (Kunegis, [2013](https://doi.org/10.1145/2487788.2488173)) databases.
The networks are stored in a format compatile with [*NEXTNet*](https://github.com/oist/NEXTNet) (*N*ext-reaction-based *E*pidemics e*X*tended to *T*emporal *Net*works), an algorithm for efficient simulation of epidemic processes on  on complex networks (including weighted and temporal networks) with arbitrary transmission and recovery time distributions.

Using [*NEXTNetR*](https://oist.github.io/NEXTNetR), the R interface to *NEXTNet*, networks from this collection can be downloaded and imported with
```
library(NEXTNetR)
empirical_network(name=...)
```
# Available networks
|Name|
|-----|
|amazon|
|asCaida|
|asOregon|
|asSkitter|
|astroPh|
|brightkite|
|condMat|
|DBLP|
|deezerEurope|
|deezerHR|
|deezerHU|
|deezerRO|
|douban|
|email|
|fbArtist|
|fbAthletes|
|fbCompany|
|fbNewSites|
|fbPublicFigures|
|flickr|
|github|
|gowalla|
|hamsterster|
|internet|
|lastfm|
|liveJournal|
|livemocha|
|museaFacebook|
|pgp|
|PIN|
|powergrid|
|roadCA|
|roadPA|
|roadTX|
|twitch|
|wordnet|
|youtube|



# Format

All networks are undirected and stored as gzip-compressed, space-separated text files of the form
```
<node1> <neighbour1> <neighbour2> ...
<node2> <neighbour2> <neighbour3> ...
```
where lines representing degree-0 nodes (i.e. nodes without neighbours) have been omitted.

