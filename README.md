# Educational LLM Response Evaluator
A comprehensive tool for evaluating AI-generated educational content quality, designed specifically for conversational educational chatbots like Raina.

## What It Does
Evaluates LLM responses for educational prompts based on multiple criteria:
- **Accuracy**: Is the content factually correct and does it answer the prompt?
- **Age-Appropriateness**: Is vocabulary and complexity suitable for the target grade level?
- **Completeness**: Does it provide sufficient detail and fully address the question?
- **Safety**: Is content appropriate and safe for students?
- **Educational Quality**: Overall educational value score (0.0-1.0)

## Features
- ✅ **Auto-incrementing results files** (results_1.csv, results_2.csv, etc.)
- ✅ **Full response evaluation** - Analyzes actual LLM outputs, not just prompts
- ✅ **Educational Quality scoring** - Specialized metric for educational content
- ✅ **Conversational tone support** - Appropriate for chatbots
- ✅ **Comprehensive test data** - 30 test cases with good and poor responses
- ✅ **Evaluator Quality tracking** - Measures how well the evaluator performs
- ✅ **Detailed CSV output** - Includes prompts, responses, and evaluation notes

## Quick Start

```bash
# Install requirements
pip install pandas

# Run the evaluator
python3 evaluate.py
```

## Example Output

```
LLM RESPONSE QUALITY EVALUATOR
========================================================

Evaluating 30 LLM responses...

Test 1: Excellent - Explain photosynthesis to a 5th grader...
Test 2: Excellent - Explain the water cycle...
Test 3: Excellent - Explain gravity simply...
...
Test 16: Poor - Explain photosynthesis to a 5th grader...
Test 17: Poor - Explain the water cycle...

========================================================
EVALUATION SUMMARY
========================================================
Total Responses Evaluated: 30
Excellent: 15
Good: 0
Needs Review: 0
Poor: 15
Safety Issues: 0

Detailed results saved to: results_6.csv

Evaluator Quality: 30/30 (100.0%)

This demonstrates:
  ✓ AI response quality assessment
  ✓ Educational content evaluation with conversational tone
  ✓ Multi-criteria evaluation framework
  ✓ Safety and appropriateness checking
  ✓ Accuracy validation against prompts
  ✓ Educational quality scoring
```

## Files
- `evaluate.py` - Main evaluation script with advanced scoring logic
- `test_prompts.csv` - 30 educational prompts with both good and poor responses
- `results_X.csv` - Auto-numbered evaluation results with comprehensive metrics

## Sample Results CSV

| Test_ID | Prompt | Response | Grade_Level | Expected_Quality | Educational_Quality | Overall_Rating | Matches_Expected | Notes |
|---------|--------|----------|-------------|-----------------|-------------------|----------------|------------------|-------|
| 1 | Explain photosynthesis... | Photosynthesis is how plants make... | 5th | Excellent | 0.95 | Excellent | True | Response meets quality standards |
| 16 | Explain photosynthesis... | Plants just eat sunlight and make stuff... | 5th | Poor | 0.1 | Poor | True | Response contains inappropriate language |

## Test Case Coverage

### Good Responses (Tests 1-15)
- Photosynthesis explanation with scientific accuracy
- Water cycle with proper terminology
- Gravity explained simply but correctly
- Fractions using relatable pizza analogy
- Comprehensive coverage of key educational topics

### Poor Responses (Tests 16-30)
- Vague or incomplete explanations
- Casual language inappropriate for education ("idk", "lol", "ngl")
- Missing key scientific concepts
- Factually incomplete or unclear information

## Evaluation Logic

The evaluator checks for:
1. **Content accuracy** - Does the response contain correct information?
2. **Key concept coverage** - Are essential terms and ideas included?
3. **Language appropriateness** - Flags severely inappropriate language while allowing conversational tone
4. **Response completeness** - Evaluates length and depth of explanation
5. **Grade-level vocabulary** - Ensures complexity matches target audience

## Updates Made
- **v1.0**: Initial prompt evaluation system
- **v2.0**: Switched to response evaluation (analyzing LLM outputs)
- **v3.0**: Added auto-incrementing file names
- **v4.0**: Added Educational Quality scoring metric
- **v5.0**: Included full responses in results CSV
- **v6.0**: Optimized for conversational chatbots (removed overly strict language filters)
- **v7.0**: Expanded test dataset to 30 cases with good/poor response pairs

## Skills Demonstrated
✓ **LLM output evaluation and quality assessment**  
✓ **Educational content analysis and scoring**  
✓ **Multi-criteria evaluation framework design**  
✓ **CSV data processing and automated reporting**  
✓ **Educational technology understanding**  
✓ **Python programming and data analysis**  
✓ **Quality assurance for AI systems**  
✓ **Understanding of conversational AI requirements**

---

*Built to showcase advanced LLM evaluation capabilities for educational AI applications
