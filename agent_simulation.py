import pandas as pd
import os

def simulate_agent_response(query, data_path):
    """
    Simple RAG-like simulation (safe version)
    """

    try:
        # --- Load data safely ---
        df = pd.read_csv(data_path)

        # --- Validate required columns ---
        required_cols = {"category", "price", "product"}
        if not required_cols.issubset(df.columns):
            return "Agent Error: Missing required columns in dataset."

        # --- Normalize query ---
        query_lower = query.lower()

        # --- Handle electronic query ---
        if "electronic" in query_lower:

            # Safe filtering (avoid NaN crash)
            subset = df[df["category"].fillna("").str.lower() == "electronics"]

            if subset.empty:
                return "Agent: Sorry, I don't see any electronics in my current knowledge base."

            # Ensure price is numeric
            subset = subset.copy()
            subset["price"] = pd.to_numeric(subset["price"], errors="coerce")
            subset = subset.dropna(subset=["price"])

            if subset.empty:
                return "Agent: No valid price data available."

            # Pick best (cheapest = best deal)
            best_deal = subset.loc[subset["price"].idxmin()]

            return (
                f"Agent: Based on my data, the best choice is "
                f"{best_deal['product']} at ${best_deal['price']}."
            )

        return "Agent: I'm not sure how to answer that with the current data."

    except FileNotFoundError:
        return f"Agent Error: Data file not found at {data_path}"

    except Exception as e:
        return f"Agent Error: Unexpected issue - {str(e)}"


# =======================
# TEST
# =======================
if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(BASE_DIR, "processed_data.csv")

    print("Testing with CLEAN data:")
    print(simulate_agent_response("What is the best electronic product?", data_path))

    print("\nTesting with GARBAGE data:")
    print(simulate_agent_response("What is the best electronic product?", "garbage_data.csv"))