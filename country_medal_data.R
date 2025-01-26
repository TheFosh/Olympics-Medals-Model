
find_country_total <- function(country_name){
	all_medals = read.csv("summerOly_medal_counts.csv")

 	country_medal = all_medals[all_medals$NOC == country_name,]

	country_total_years = country_medal[, c('Total', 'Year')]
}