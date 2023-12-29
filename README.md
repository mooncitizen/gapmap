[![Release](https://github.com/mooncitizen/gapmap/actions/workflows/pypi.yaml/badge.svg)](https://github.com/mooncitizen/gapmap/actions/workflows/pypi.yaml)


![alt text](/images/logo150.png)

## GAPMAP

A helper library that makes pathing simple in the real world. Point to Point distance finding and even Placename finding.

Roadmap

- [x] Placename finder (City, Country)
- [x] Euclidean Distances
- [] GIS based Pathing
- [] GIS Based timing
- [] Map Generation
- [] Hotswapping hosted maps


# Euclidean Distance
This can simply be described as stright line distance or as the crow flys. This will not be accurate in terms of finding ranges where there is a route to be adhered to. Its more of an indication rather than guidance. But can help build a picture between points. For example you could levy a percentage of overage to be applied that could guestimate that an area is out of range. However this is exponentially bad when the direct line distance is great. It might be good for something within 20 miles but not at 100 miles. A great starting resource would be to read [Euclidean Distance Formula - CUEMATH](https://www.cuemath.com/euclidean-distance-formula/)

# Purpose

The purpose of this library is to grow it into a trusted framework of getting real world distance finding for land, sea and air using real world restrictions. The ability to create pathing in a unified form to work with the likes of <b>Google Maps</b> and <b>Mapbox</b>

# End Goal
To create a machine/ai learned process that predict routing, pathing and distance. But got to start somewhere

