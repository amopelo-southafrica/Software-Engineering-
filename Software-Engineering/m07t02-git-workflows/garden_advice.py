def get_season_advice(season):
    """Return gardening advice based on the season."""
    
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Prune plants and prepare soil for new growth.",
        "autumn": "Remove dead leaves and prepare plants for colder weather."
    }

    return season_advice.get(season.lower(), "No advice for this season.")


def get_plant_advice(plant_type):
    """Return gardening advice based on plant type."""
    
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Ensure proper drainage to avoid root rot."
    }

    return plant_advice.get(plant_type.lower(), "No advice for this type of plant.")


def main():
    """Main function to run the gardening advice program."""
    
    season = input("Enter the season: ")
    plant_type = input("Enter the plant type: ")

    season_message = get_season_advice(season)
    plant_message = get_plant_advice(plant_type)

    print("\nGardening Advice:")
    print(season_message)
    print(plant_message)


if __name__ == "__main__":
    main()
