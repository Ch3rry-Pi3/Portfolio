import pandas as pd

def count_experiments(experiments: pd.DataFrame) -> pd.DataFrame:
    """
    Counts the number of experiments conducted on each platform for each experiment type.
    Ensures that all (platform, experiment_name) pairs are included, even if no experiments exist.

    Args:
        experiments (pd.DataFrame): A DataFrame containing experiment details with columns:
                                    - "experiment_id" (int): Unique ID of the experiment.
                                    - "platform" (str): Platform used ('Android', 'IOS', 'Web').
                                    - "experiment_name" (str): Experiment type ('Reading', 'Sports', 'Programming').

    Returns:
        pd.DataFrame: A DataFrame with columns:
                      - "platform" (str): The platform name.
                      - "experiment_name" (str): The experiment type.
                      - "num_experiments" (int): The count of experiments for each platform-experiment pair.
    """

    # Define all possible platform and experiment name combinations
    platforms = pd.DataFrame({'platform': ['Android', 'IOS', 'Web']})
    experiment_names = pd.DataFrame({'experiment_name': ['Reading', 'Sports', 'Programming']})

    # Create a complete cross-product of platforms and experiment names
    all_combinations = platforms.merge(experiment_names, how='cross')

    # Group by platform and experiment name, counting occurrences
    experiment_counts = (
        experiments
        .groupby(['platform', 'experiment_name'])
        .size()
        .reset_index(name='num_experiments')
    )

    # Merge with all possible combinations to ensure missing values are included
    result = all_combinations.merge(experiment_counts, on=['platform', 'experiment_name'], how='left').fillna(0)

    return result


if __name__ == "__main__":
    # Example input
    data = {
        "experiment_id": [4, 13, 9, 12, 18],
        "platform": ["IOS", "IOS", "Android", "Web", "Web"],
        "experiment_name": ["Programming", "Sports", "Reading", "Reading", "Programming"]
    }
    experiments_df = pd.DataFrame(data)

    # Compute and display results
    output_df = count_experiments(experiments_df)
    print(output_df)
