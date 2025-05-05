# Import required libraries
import PyPDF2  # type: ignore
import re  # Import regex module for pattern matching

# Path to your PDF file
pdf_path = "MCQS Workbook.pdf"  # Make sure this file exists in your project directory

# Open the PDF file for reading
with open(pdf_path, "rb") as file:
    # Initialize a PDF reader to extract text
    reader = PyPDF2.PdfReader(file)  # Reads the PDF file
    total_pages = len(reader.pages)  # Get the total number of pages in the PDF
    print(f"Total pages in PDF: {total_pages}")  # Display total pages

    # Initialize an empty string to store extracted text
    all_text = ""
    
    # Loop through all pages of the PDF to extract text
    for i in range(total_pages):
        try:
            page = reader.pages[i]  # Access the ith page of the PDF
            text = page.extract_text()  # Extract text from the page
            if text:
                all_text += f"\n{text}"  # Add extracted text to the all_text variable
        except IndexError:
            print(f"Page {i + 1} out of range.")  # Error handling for out-of-range page

# Clean up extracted text
# Remove occurrences of "Page X" (like "Page 5") from the text
all_text = re.sub(r'Page\s*\d+', '', all_text)

# Replace multiple newlines with a single newline
all_text = re.sub(r'\n+', '\n', all_text).strip()  # Strip leading and trailing spaces

# --------------------------
# Regex Patterns for Extraction
# --------------------------

# Pattern for extracting MCQs: Looks for numbered lines followed by options (a), (b), (c), etc.
mcq_pattern = re.compile(
    r'(\d+\.\s*.*?(?:\([a-dA-D]\)\s*.*?)+)(?=\n\d+\.|\Z)',  # Regex pattern to capture MCQs
    re.DOTALL  # Allows matching across multiple lines
)

# Pattern for extracting Descriptive Questions: Looks for sentences ending with a "?"
descriptive_pattern = re.compile(
    r'(\d+\.\s*[A-Z][^\n]+\?)',  # Regex pattern to capture descriptive questions
    re.MULTILINE  # Makes sure it matches across multiple lines
)

# --------------------------
# Extract Questions Using the Defined Patterns
# --------------------------

# Use the MCQ regex pattern to find all MCQs in the text
mcqs = mcq_pattern.findall(all_text)

# Use the descriptive question regex pattern to find all descriptive questions
descriptive_questions = descriptive_pattern.findall(all_text)

# --------------------------
# Output the Extracted Questions
# --------------------------

# Print extracted MCQs
print("\n--- Extracted Multiple Choice Questions (MCQs) ---\n")
if mcqs:
    # Loop through all found MCQs and display them
    for idx, mcq in enumerate(mcqs, 1):
        print(f"MCQ {idx}: {mcq.strip()}\n")
else:
    print("No multiple-choice questions found.")  # If no MCQs are found

# Print extracted Descriptive Questions
print("\n--- Extracted Descriptive Questions ---\n")
if descriptive_questions:
    # Loop through all found descriptive questions and display them
    for idx, question in enumerate(descriptive_questions, 1):
        print(f"Descriptive Question {idx}: {question.strip()}\n")
else:
    print("No descriptive questions found.")  # If no descriptive questions are found
