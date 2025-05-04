import argparse
from rag.pipeline import build_db, query_rag_system

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true", help="Build the vector database")
    parser.add_argument("--query", type=str, help="Ask a question")
    parser.add_argument("--data_dir", type=str, default="../data/")
    args = parser.parse_args()

    if args.build:
        build_db(args.data_dir)
    elif args.query:
        answer, metadata = query_rag_system(args.query)
        print("Answer:\n", answer)
        print("\nSources:")
        for meta in metadata:
            print("-", meta.get("source", "Unknown"))
    else:
        parser.print_help()