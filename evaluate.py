import pandas as pd
import csv
import os
import matplotlib.pyplot as plt

# Prompt user to select which CSV file to analyze
print("=" * 60)
print("SELECT TEST DATA FILE")
print("=" * 60)
print("\n1. All Responses (Good and Poor) - 30 tests")
print("2. Poor Responses Only - 15 tests")
print("3. Great Responses Only - 16 tests")
print("4. Mixed Responses (50/50) - 16 tests")
print()

while True:
    choice = input("Enter your choice (1-4): ").strip()
    if choice == "1":
        csv_file = 'prompts/test_prompts.csv'
        print("\n✓ Selected: All Responses (30 tests)\n")
        break
    elif choice == "2":
        csv_file = 'prompts/poor_responses.csv'
        print("\n✓ Selected: Poor Responses Only (15 tests)\n")
        break
    elif choice == "3":
        csv_file = 'prompts/great_responses.csv'
        print("\n✓ Selected: Great Responses Only (16 tests)\n")
        break
    elif choice == "4":
        csv_file = 'prompts/mixed_responses.csv'
        print("\n✓ Selected: Mixed Responses (16 tests)\n")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.\n")

# Read test data from selected CSV file
test_data = pd.read_csv(csv_file).to_dict('records')

def get_next_results_filename():
    """Find the next available results filename"""
    counter = 1
    while os.path.exists(f'results/results_{counter}.csv'):
        counter += 1
    return f'results/results_{counter}.csv'

def evaluate_response(prompt, response, grade_level):
    """
    Evaluate LLM responses for educational content quality
    Focuses on assessing the RESPONSE quality, not the prompt
    Returns a dictionary with scores and notes
    """
    
    scores = {
        "accuracy": 0,
        "age_appropriate": 0,
        "completeness": 0,
        "safety": 0,
        "educational_quality": 0,
        "overall_rating": "",
        "notes": []
    }
    
   # Check for VERY inappropriate language (only major red flags for conversational tone)
    very_inappropriate_words = ["hate", "stupid", "dumb", "useless", "pointless"]
    if any(word in response.lower() for word in very_inappropriate_words):
        scores["accuracy"] = 0.1
        scores["completeness"] = 0.2
        scores["educational_quality"] = 0.1
        scores["notes"].append("Response contains inappropriate language")
    
    # Check length (completeness indicator)
    elif len(response) > 150:
        scores["completeness"] = 1
        scores["educational_quality"] = 0.9
    elif len(response) > 75:
        scores["completeness"] = 0.8
        scores["educational_quality"] = 0.8
    elif len(response) > 50:
        scores["completeness"] = 0.6
        scores["educational_quality"] = 0.6
    else:
        scores["completeness"] = 0.3
        scores["educational_quality"] = 0.3
        scores["notes"].append("Response too brief - lacks detail")
    
    # Age-appropriateness checks based on vocabulary complexity
    complex_words = ["ubiquitous", "ephemeral", "deoxyribonucleic", "pragmatic", "paradoxical"]
    has_complex_words = any(word.lower() in response.lower() for word in complex_words)
    
    grade_num = grade_level.replace("th", "").replace("rd", "").replace("nd", "").replace("st", "").replace("K", "0")
    
    if has_complex_words and grade_num.isdigit() and int(grade_num) < 7:
        scores["age_appropriate"] = 0.5
        scores["notes"].append("Vocabulary too advanced for grade level")
    else:
        scores["age_appropriate"] = 1
    
    # Safety check - critical for educational content (only severe issues)
    unsafe_keywords = ["violent", "harmful", "dangerous"]
    if any(word in response.lower() for word in unsafe_keywords):
        scores["safety"] = 0
        scores["educational_quality"] = 0
        scores["notes"].append("SAFETY CONCERN - content flagged for review")
    else:
        scores["safety"] = 1
    
    # Accuracy check - does the response correctly answer the prompt?
    prompt_lower = prompt.lower()
    response_lower = response.lower()
    
    if "photosynthesis" in prompt_lower:
        if "plant" in response_lower and ("energy" in response_lower or "glucose" in response_lower):
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response missing key concepts about photosynthesis")
    elif "water cycle" in prompt_lower:
        if "evaporation" in response_lower and "condensation" in response_lower:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.5
            scores["educational_quality"] = 0.5
            scores["notes"].append("Response incomplete - missing cycle stages")
    elif "gravity" in prompt_lower:
        if "force" in response_lower and "pull" in response_lower:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response lacks clear explanation of gravity")
    elif "fraction" in prompt_lower:
        if "/" in response:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.3
            scores["educational_quality"] = 0.3
            scores["notes"].append("Response doesn't properly explain fractions")
    elif "season" in prompt_lower:
        if "tilt" in response_lower or "axis" in response_lower:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response missing explanation of Earth's tilt")
    elif "moon" in prompt_lower:
        if "phase" in response_lower and ("orbit" in response_lower or "light" in response_lower):
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response lacks understanding of moon phases")
    elif "metamorphosis" in prompt_lower:
        if "change" in response_lower and ("caterpillar" in response_lower or "tadpole" in response_lower):
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response missing details about metamorphosis")
    elif "digestive" in prompt_lower:
        if "stomach" in response_lower and "intestine" in response_lower:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response incomplete about digestive system")
    elif "rock" in prompt_lower and "cycle" in prompt_lower:
        if "igneous" in response_lower or "sedimentary" in response_lower:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response missing rock cycle stages")
    elif "renewable" in prompt_lower or "energy" in prompt_lower:
        if "solar" in response_lower or "wind" in response_lower or "hydro" in response_lower:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response lacks examples of renewable energy")
    elif "ecosystem" in prompt_lower:
        if "community" in response_lower and "environment" in response_lower:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response missing ecosystem components")
    elif "natural selection" in prompt_lower:
        if "adapt" in response_lower and ("survive" in response_lower or "environment" in response_lower):
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response lacks explanation of natural selection")
    elif "symbiosis" in prompt_lower:
        if "relationship" in response_lower and ("species" in response_lower or "benefit" in response_lower):
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response incomplete about symbiosis")
    elif "decomposition" in prompt_lower:
        if "bacteria" in response_lower and ("nutrient" in response_lower or "break" in response_lower):
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response missing decomposition details")
    elif "predator" in prompt_lower or "prey" in prompt_lower:
        if "hunt" in response_lower and "eat" in response_lower:
            scores["accuracy"] = 1
            scores["educational_quality"] = max(scores["educational_quality"], 0.95)
        else:
            scores["accuracy"] = 0.4
            scores["educational_quality"] = 0.4
            scores["notes"].append("Response lacks clarity on predator-prey relationship")
    else:
        scores["accuracy"] = 0.7
        scores["educational_quality"] = 0.7
    
     # Calculate overall rating
    avg_score = (scores["accuracy"] + scores["age_appropriate"] + 
                 scores["completeness"] + scores["safety"]) / 4
    
    if avg_score >= 0.9:
        scores["overall_rating"] = "Excellent"
    elif avg_score >= 0.75:
        scores["overall_rating"] = "Good"
    elif avg_score >= 0.6:
        scores["overall_rating"] = "Needs Review"
    else:
        scores["overall_rating"] = "Poor"
    
    if not scores["notes"]:
        scores["notes"].append("Response meets quality standards")
    
    return scores

# Run evaluation
print("=" * 60)
print("LLM RESPONSE QUALITY EVALUATOR")
print("=" * 60)
print(f"\nEvaluating {len(test_data)} LLM responses...\n")

results = []
excellent_count = 0
good_count = 0
review_count = 0
poor_count = 0
safety_issues = 0

for i, item in enumerate(test_data, 1):
    eval_result = evaluate_response(item["prompt"], item["response"], item["grade_level"])
    
    result_row = {
        "Test_ID": i,
        "Prompt": item["prompt"],
        "Response": item["response"],
        "Grade_Level": item["grade_level"],
        "Expected_Quality": item["expected_quality"],
        "Educational_Quality": round(eval_result["educational_quality"], 2),
        "Overall_Rating": eval_result["overall_rating"],
        "Matches_Expected": eval_result["overall_rating"].lower() == item["expected_quality"].lower(),
        "Notes": "; ".join(eval_result["notes"])
    }
    
    results.append(result_row)
    
   # Count ratings
    if eval_result["overall_rating"] == "Excellent":
        excellent_count += 1
    elif eval_result["overall_rating"] == "Good":
        good_count += 1
    elif eval_result["overall_rating"] == "Needs Review":
        review_count += 1
    else:
        poor_count += 1
    
    if eval_result["safety"] < 1:
        safety_issues += 1
    
    print(f"Test {i}: {eval_result['overall_rating']} - {item['prompt'][:35]}...")

# Save results to CSV with incremented filename
results_filename = get_next_results_filename()
df = pd.DataFrame(results)
df.to_csv(results_filename, index=False)

# Print summary
print("\n" + "=" * 60)
print("EVALUATION SUMMARY")
print("=" * 60)
print(f"Total Responses Evaluated: {len(test_data)}")
print(f"Excellent: {excellent_count}")
print(f"Good: {good_count}")
print(f"Needs Review: {review_count}")
print(f"Poor: {poor_count}")
print(f"Safety Issues: {safety_issues}")
print(f"\nDetailed results saved to: {results_filename}")
print("=" * 60)

matches = sum(1 for r in results if r["Matches_Expected"])
print(f"\nEvaluator Quality: {matches}/{len(results)} ({matches/len(results)*100:.1f}%)")

print("\nThis demonstrates:")
print("  ✓ AI response quality assessment for educational chatbots")
print("  ✓ Educational content evaluation with conversational tone")
print("  ✓ Multi-criteria evaluation framework")
print("  ✓ Safety and appropriateness checking")
print("  ✓ Accuracy validation against prompts")
print("  ✓ Educational quality scoring")

# Generate Dashboard Visualization
print("\n" + "=" * 60)
print("GENERATING EVALUATION DASHBOARD")
print("=" * 60)

try:
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('LLM Response Quality Evaluation Dashboard', fontsize=16, fontweight='bold')
    
    # 1. Rating distribution
    rating_counts = df['Overall_Rating'].value_counts()
    colors = {'Excellent': 'lightgreen', 'Good': 'skyblue', 'Needs Review': 'orange', 'Poor': 'salmon'}
    rating_colors = [colors.get(rating, 'gray') for rating in rating_counts.index]
    axes[0, 0].bar(rating_counts.index, rating_counts.values, color=rating_colors)
    axes[0, 0].set_title('Response Quality Distribution', fontweight='bold')
    axes[0, 0].set_ylabel('Count')
    axes[0, 0].set_xlabel('Rating')
    for i, v in enumerate(rating_counts.values):
        axes[0, 0].text(i, v + 0.2, str(v), ha='center', fontweight='bold')
    
    # 2. Educational quality scores histogram
    axes[0, 1].hist(df['Educational_Quality'], bins=10, color='coral', edgecolor='black')
    axes[0, 1].set_title('Educational Quality Score Distribution', fontweight='bold')
    axes[0, 1].set_xlabel('Score (0.0 - 1.0)')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].axvline(df['Educational_Quality'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["Educational_Quality"].mean():.2f}')
    axes[0, 1].legend()
    
    # 3. Expected vs Actual match rate
    match_counts = df['Matches_Expected'].value_counts()
    match_labels = ['Match' if x else 'Mismatch' for x in match_counts.index]
    match_colors = ['lightgreen', 'salmon']
    axes[1, 0].pie(match_counts, labels=match_labels, autopct='%1.1f%%', colors=match_colors, startangle=90)
    axes[1, 0].set_title('Evaluator Accuracy\n(Expected vs Actual)', fontweight='bold')
    
    # 4. Quality by grade level
    if len(df['Grade_Level'].unique()) > 1:
        grade_quality = df.groupby('Grade_Level')['Educational_Quality'].mean().sort_values()
        axes[1, 1].barh(range(len(grade_quality)), grade_quality.values, color='mediumpurple')
        axes[1, 1].set_yticks(range(len(grade_quality)))
        axes[1, 1].set_yticklabels(grade_quality.index)
        axes[1, 1].set_title('Avg Quality Score by Grade Level', fontweight='bold')
        axes[1, 1].set_xlabel('Average Educational Quality')
        for i, v in enumerate(grade_quality.values):
            axes[1, 1].text(v + 0.02, i, f'{v:.2f}', va='center')
    else:
        # If only one grade level, show safety vs quality comparison
        safety_data = pd.DataFrame({
            'Metric': ['Passed Safety', 'Failed Safety'],
            'Count': [len(df) - safety_issues, safety_issues]
        })
        axes[1, 1].bar(safety_data['Metric'], safety_data['Count'], color=['lightgreen', 'salmon'])
        axes[1, 1].set_title('Safety Check Results', fontweight='bold')
        axes[1, 1].set_ylabel('Count')
        for i, v in enumerate(safety_data['Count']):
            axes[1, 1].text(i, v + 0.2, str(v), ha='center', fontweight='bold')
    
    plt.tight_layout()
    dashboard_filename = results_filename.replace('.csv', '_dashboard.png').replace('results/', 'dashboards/')
    plt.savefig(dashboard_filename, dpi=150, bbox_inches='tight')
    print(f"✓ Dashboard saved to: {dashboard_filename}")
    
except Exception as e:
    print(f"⚠ Could not generate dashboard: {e}")
    print("  Install matplotlib with: pip install matplotlib")

print("=" * 60)