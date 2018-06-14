library(httr)
#This is a function that geocodes addresses using the GeoCoding Census API. 
geocoding_api <- function(street, city, state, zip) {
  base_url = "https://geocoding.geo.census.gov/geocoder/geographies/address?benchmark=Public_AR_Census2010&format=json&vintage=Census2010_Census2010&layers=14&"
  street = paste("&street=", street, sep = "")
  city = paste("&city=", city, sep = "")
  state = paste("&state=", state, sep = "")
  zip = paste("&zip=", zip, sep = "")
  #Concatenates each command to the 
  req_url = paste(base_url, street, city, state, zip, sep = "")
  req <- GET(req_url)
  resp <- content(req)
  location_data = data.frame(
    x = resp$result$addressMatches[[1]]$coordinates$x,
    y = resp$result$addressMatches[[1]]$coordinates$y,
    geo.id = resp$result$addressMatches[[1]]$geographies$`Census Blocks`[[1]]$GEOID
  )
  location_data
}
x <- geocoding_api("5619+Belarbor+Street","Houston","TX","77033")

