def print_results(results):
    for target, metrics in results.items():
        print(f"\nÉvaluation pour {target}:")
        for model_name, metric in metrics.items():
            print(f"{model_name} - MSE: {metric['MSE']}, R2: {metric['R2']}")
