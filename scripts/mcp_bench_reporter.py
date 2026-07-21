"""
Modular AI Performance Benchmarking & Auto-Reporting Engine.
Measures execution velocities and handles automated timestamped archival tracking.
"""
import subprocess
import json
import time
import sys
import os
import pandas as pd

def execute_bench_and_report():
    print("====================================================================")
    print("📈 RUNNING PROGRAMMATIC PERFORMANCE BENCHMARK & GRAPH VISUALIZER")
    print("====================================================================\n")

    target_script = "src/dalio_sovereign_strength_index/app_mcp.py"
    iterations = 50
    execution_times = []
    last_payload = None

    print(f"[Benchmark] Processing {iterations} tool calls down the MCP channel...")
    start_total_time = time.perf_counter()
    
    for i in range(iterations):
        penalty_variant = 1.0 + (i * 0.02)
        mock_request = {
            "jsonrpc": "2.0", "id": i, "method": "tools/call",
            "params": {"arguments": {"start_year": 2018, "end_year": 2025, "debt_weight_penalty": penalty_variant}}
        }
        
        loop_start = time.perf_counter()
        process = subprocess.Popen(
            [sys.executable, target_script],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        stdout_output, _ = process.communicate(input=json.dumps(mock_request) + "\n")
        loop_end = time.perf_counter()
        
        execution_times.append(loop_end - loop_start)
        if i == iterations - 1:
            last_payload = stdout_output

    total_duration = time.perf_counter() - start_total_time
    avg_speed = sum(execution_times) / len(execution_times)

    # Export main CSV tracking file
    bench_df = pd.DataFrame({'Iteration': range(1, iterations + 1), 'Response_Time_MS': [t * 1000 for t in execution_times]})
    bench_df.to_csv("docs/mcp_performance_trends.csv", index=False)

    # Parse final content data payload blocks
    response_json = json.loads(last_payload)
    
    # FIX: Correctly index the first item [0] of the content list before querying the text string key
    raw_text_payload = response_json["result"]["content"][0]["text"]
    records = json.loads(raw_text_payload)
    
    us_2025 = next(item for item in records if item["year"] == 2025 and item["Country"] == "US")
    cn_2025 = next(item for item in records if item["year"] == 2025 and item["Country"] == "CN")

    report_text = f"""====================================================================
📊 SYSTEMIC SOVEREIGN RISK AUTO-COMPILED ANALYTICS REPORT
====================================================================
Generated Run Status: SUCCESS
Total Benchmark Suite Duration: {total_duration:.4f} seconds
Mean Stream Processing Velocity: {avg_speed * 1000:.2f} milliseconds / tool call
--------------------------------------------------------------------
💥 FORECAST SYSTEM CONFLICT FRONTIER SNAPSHOT (YEAR 2025)
--------------------------------------------------------------------
🇺🇸 US Power Index Vector : {us_2025['Dalio_Power_Index']:.4f} | State: {us_2025['Stage_Status']}
🇨🇳 CN Power Index Vector : {cn_2025['Dalio_Power_Index']:.4f} | State: {cn_2025['Stage_Status']}
===================================================================="""

    with open("docs/macro_summary_report.txt", "w") as f:
        f.write(report_text)

    # Automated file system replication archiving runs under unique timestamp names
    os.makedirs("docs/archive", exist_ok=True)
    timestamp = int(time.time())
    
    bench_df.to_csv(f"docs/archive/mcp_performance_trends_{timestamp}.csv", index=False)
    with open(f"docs/archive/macro_summary_report_{timestamp}.txt", "w") as f:
        f.write(report_text)
        
    print(f"✅ Main reporting files updated. Unique historical run archived to docs/archive/")
    print(report_text)

if __name__ == "__main__":
    execute_bench_and_report()
