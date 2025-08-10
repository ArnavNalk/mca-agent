from answer_question import answer_query

results = answer_query("which companies were investigated for fraud in 2007", k=5)

for i, (chunk, metadata) in enumerate(results, 1):
    print(f"\n🔹 Result {i}")
    print(f"📄 Source: {metadata}")
    print(f"📝 Text: {chunk}")