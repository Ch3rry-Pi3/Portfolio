import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    """
    Determines the type of weather for each country in November 2019.

    Args:
        countries (pd.DataFrame): DataFrame containing country_id and country_name.
        weather (pd.DataFrame): DataFrame containing country_id, weather_state, and day.

    Returns:
        pd.DataFrame: A DataFrame with country_name and weather_type.
    """

    # Filter for weather data in November
    weather_nov = weather[weather["day"].dt.month == 11]

    # Compute the average weather_state per country
    avg_weather = (
        weather_nov.groupby("country_id", as_index=False)["weather_state"]
        .mean()
        .assign(
            weather_type=lambda df: df["weather_state"].map(
                lambda x: "Hot" if x >= 25 else "Cold" if x <= 15 else "Warm"
            )
        )
    )

    # Merge with countries data to get country names
    result = (
        countries.merge(avg_weather, on="country_id", how="left")
        [["country_name", "weather_type"]]
        .dropna(subset=["weather_type"])                # Remove countries with no weather data
    )

    return result


def main():
    """
    Runs example test cases for the weather_type function.
    """
    # Example Countries DataFrame
    countries_data = {
        "country_id": [1, 2, 3],
        "country_name": ["USA", "Canada", "Mexico"],
    }
    countries = pd.DataFrame(countries_data)

    # Example Weather DataFrame
    weather_data = {
        "country_id": [1, 1, 2, 2, 3, 3],
        "weather_state": [30, 28, 10, 12, 20, 26],
        "day": pd.to_datetime(["2019-11-01", "2019-11-15", "2019-11-10", "2019-11-25", "2019-11-05", "2019-11-20"]),
    }
    weather = pd.DataFrame(weather_data)

    # Run function and print results
    result = weather_type(countries, weather)
    print(result)


if __name__ == "__main__":
    main()
