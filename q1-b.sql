select country.code,count(city.name) from country, city where country.code=city.countrycode group by country.code order by country.code;