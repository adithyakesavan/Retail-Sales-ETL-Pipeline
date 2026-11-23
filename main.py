
import subprocess
import sys
from pathlib import Path


# Find project root directory
BASE_DIR = Path(__file__).resolve().parent


def run_step(step_name, script_name):

    print("\n" + "=" * 60)
    print(f"STARTING: {step_name}")
    print("=" * 60)

    script_path = BASE_DIR / "src" / script_name

    # Execute each pipeline stage using the same Python environment
    subprocess.run(
        [sys.executable, str(script_path)],
        cwd=BASE_DIR,
        check=True
    )

    print(f"\nCOMPLETED: {step_name}")


def main():

    print("\nRETAIL SALES ETL PIPELINE")
    print("END-TO-END EXECUTION STARTED")

    try:

        # Stage 1: Extract and transform
        run_step(
            "DATA EXTRACTION AND TRANSFORMATION",
            "transform.py"
        )

        # Stage 2: Load into SQLite
        run_step(
            "DATABASE LOADING",
            "load.py"
        )

        # Stage 3: SQL analytics
        run_step(
            "BUSINESS ANALYTICS",
            "run_analytics.py"
        )

        print("\n" + "=" * 60)
        print("ETL PIPELINE COMPLETED SUCCESSFULLY!")
        print("=" * 60)

    except subprocess.CalledProcessError as error:

        print("\nPIPELINE FAILED!")
        print(f"Failed script: {error.cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
