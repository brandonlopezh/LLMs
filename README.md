# Educational LLM Response Evaluator

A simple tool for evaluating AI-generated educational content quality.

## What It Does
Evaluates LLM responses for educational prompts based on:
- **Accuracy**: Is the content factually correct?
- **Age-Appropriateness**: Is it suitable for the target grade level?
- **Completeness**: Does it fully answer the prompt?
- **Safety**: Is it appropriate for students?

## Quick Start

```bash
# Install requirements
pip install pandas

# Run the evaluator
python evaluate.py
```

## Example Output

```
Evaluating 10 educational prompts...

Results:
- 8/10 responses rated "Good" or "Excellent"
- 2/10 flagged for review (too complex language)
- 0 safety issues found

See results.csv for details
```

## Files
- `evaluate.py` - Main evaluation script
- `test_prompts.csv` - Sample educational prompts and responses
- `results.csv` - Evaluation results with scores and notes

## Sample Test Cases

| Prompt | Grade Level | Response Quality | Issues Found |
|--------|-------------|------------------|--------------|
| "Explain photosynthesis" | 5th grade | Good | None |
| "Create a quiz on fractions" | 4th grade | Needs Review | Questions too hard |
| "Write a history summary" | 8th grade | Excellent | None |

## Skills Demonstrated
✓ LLM output evaluation  
✓ Educational content assessment  
✓ Data organization in spreadsheets  
✓ Pattern identification  
✓ Clear documentation  

---

*Built to showcase LLM quality analysis skills for educational AI applications*
