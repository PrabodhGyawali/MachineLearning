Root URL: `https://www.zoopla.co.uk/house-prices/oxford/?pn=41`
- iterate through `?pn={i}`

Features:
- Number of Beds
- Number of Baths
- Number of Receptions
- Type: T, mid-T, semi-D, D, Flat, 
- EPC rating
- Square meter
- Time sold
- Freehold: Y or N

More detail on property url:
`https://www.zoopla.co.uk/property/uprn/{id}/`
- Id has no pattern

May need to extract the url to each of the property and send a get request ot get more data
