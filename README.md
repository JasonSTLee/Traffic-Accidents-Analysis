# 🚗 Traffic Accidents Analysis 

In this project, I simulate working as an **analyst for an insurance company looking to find zipcodes that are prone to having frequent accidents.** The goal is to identify correlations and patterns between accidents, weather patterns, and demographic information such as population, commuting times, and number of car owners. By understanding the causes of accidents in specific areas, I aim to adjust insurance premiums based on the different factors in each zip code. This analysis enables data-driven decision making for pricing insurance.

## Datasets Used
- [Accident data](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
- [American Community Survey](https://www.census.gov/data/developers/data-sets/acs-5year.html)
- [Zipcodes to ZCTA Crosswalk](https://github.com/censusreporter/acs-aggregate/blob/master/crosswalks/zip_to_zcta/ZIP_ZCTA_README.md)
  
## Tech Used
- Python (libraries: Pandas, OS, Matplotlib, and Alpha Vantage)
- American Community Survey api
- Historical Weather api
- [Nominatim api](https://nominatim.org/) (Latitude and Longitude data)

**Notebook can be found [here](https://github.com/JasonSTLee/Traffic-Accidents-Analysis/blob/main/main.ipynb)**

## Questions to ask

**1a.** Do more accidents occur with more people for each zipcode?
![output](https://github.com/user-attachments/assets/2d864438-7da3-4fef-af00-0b8efbc1d05d)

There is a direct correlation between the population count and number of accidents per zipcode. While there are zipcodes with high population and low accidents, those are the exception and not the rule.

---

**1b.** Does the number of commuters via car and car owners correlate to numbers of accidents?
![output2](https://github.com/user-attachments/assets/7fede9bd-e33b-4a92-bdff-a4c409d4878e)

Similar to the graph above, there are direct correlations for number of car owners, commuters via car and the number of accidents.

---

**2.** What time do most accidents occur?
![output3](https://github.com/user-attachments/assets/da774f98-92d2-4578-9372-fcdf780ed565)

Accidents occur around rush hour times when commuters are driving to work and back to home around: 6am - 8am and 2pm - 5pm. This aligns when most people are driving, although I am surprised that number of accidents lower signicantly at 7pm.

---

**3.** Is there an increase of accidents during rush hours?
![output4](https://github.com/user-attachments/assets/497b5199-10a6-4341-a7d9-56c5d662a002)

For hours where most accidents occur, there is a gradual year over year increase with the exception of a dip during the pandemic. This dip most is most likely caused by the overall number of drivers decreasing due to the lockdown. However post-pandemic numbers show that there is a continuous increase, highlighting a return to growth after lockdown during all hours.

---

**4.** Is there an increase outside of rush hours?
![output5](https://github.com/user-attachments/assets/9e8ad7cc-a198-4664-ab6c-1f7f45baa9c8)

By adding the number of accidents for high accident & non high accident hours, we're able to see an interesting trend. Rush hour accidents increase steadily over time, while non-rush hour accidents have years of decrease. While there are more accidents occuring outside of non-rush hours, the number doesn't consistently grow like the rush hour accidents. 

---

**5.** How does weather affect car accidents?
![output6](https://github.com/user-attachments/assets/3d18e8a2-549c-4285-8a9e-6d4e6fa3b814)

This graph shows 4 pie charts of varying car accident severity. Within each of the 4 severity categories, it is then further broken down by weather severity. There are a few interesting points to note here

- Regardless of the severity of the accident, the weather severity is consistent throughout. Meaning that more dangerous weather doesn't necessarily mean a higher accident severity.
- Most accidents occur in dangerous weather conditions, indicating that dangerous weather is persistent throughout ~60% of all accidents

---

## Conclusions

To begin with finding zipcodes that have a high number of bad accidents, below are zipcodes with the highest percentage of total accidents that are high in accident and weather severity.
![output7](https://github.com/user-attachments/assets/071952f4-299f-479a-8995-42f260d6421a)

We have confirmed these metrics are correlated to the number of accidents that occur in each zip code:
- Population
- Number of commuters using cars
- Number of car owners
- Number of drivers during high accident hours
I ranked the zipcode by it's year over year growth/decline for each metric, 1 being the highest growth, essentially creating a sorted row number for each metric. After that, I added all the row numbers together. Remember that the lower the number, the higher the risk of accidents occuring within that zipcode. Below are the top 10 zipcodes that are most prone to accidents.
![output8](https://github.com/user-attachments/assets/77094d63-4839-41cc-853b-a32b901ce902)

### Limitations of Dataset
1. I'm unable to get historical weather data for every zip code because of the api limitations and pricing
