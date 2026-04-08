from importlib.util import find_spec
from importlib.metadata import version


def checking_dependencies() -> bool:
    status = True
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    requirements = [
        {
            "name": "numpy",
            "status": "KO",
            "version": "not available",
            "type": "Numerical computation",
            "state": "is not ready",
        },
        {
            "name": "pandas",
            "status": "KO",
            "version": "not available",
            "type": "Data manipulation",
            "state": "is not ready",
        },
        {
            "name": "matplotlib",
            "status": "KO",
            "version": "not available",
            "type": "Visualization",
            "state": "is not ready",
        },
    ]

    for libs in requirements:
        if find_spec(libs["name"]) is not None:
            libs["status"] = "OK"
            libs["version"] = version(libs["name"])
            libs["state"] = "ready"
        else:
            status = False
    for libs in requirements:
        print(
            f"[{libs['status']}] {libs['name']} {libs['version']} - "
            f"{libs['type']} {libs['state']}"
        )
    return status


def process_data_brother() -> None:
    if checking_dependencies() is True:
        print()
        data = process_data()
        stats = analyze_data(data)
        generate_visual(data)
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png\n")
        print(f"Minumun value of the graph is {stats['minimum']}")
        print(f"Maximum value of the graph is {stats['maximum']}")
    else:
        print(
            "Missing some required packages, "
            "import the right packages and try again!"
        )


def process_data() -> Any:
    print("Processing 1000 data points...")
    import pandas
    import numpy

    x_values = numpy.linspace(0, 10, 1000)
    df = pandas.DataFrame({"x": x_values, "y": numpy.cos(x_values)})
    return df


def analyze_data(df: Any) -> dict:
    print("Analyzing Matrix data...")
    stats = {"minimum": df["y"].min(), "maximum": df["y"].max()}
    return stats


def generate_visual(df: Any) -> None:
    print("Generating visualization...")
    import matplotlib.pyplot as pl

    pl.plot(df["x"], df["y"], label="cos(x)", color="blue")
    pl.title("Cosinus function")
    pl.savefig("matrix_analysis")


if __name__ == "__main__":
    process_data_brother()
