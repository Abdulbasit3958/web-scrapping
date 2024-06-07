# Web-scrapping


Sure! I'll update the README according to the provided repository name and incorporate the details from the source code files. Here's the revised README:

---

## Web Scraping

### Repository: web-scrapping

This repository contains Python scripts for scraping job listings from two popular job portals: Indeed and Bayt. The scripts are designed to extract job titles, companies, locations, and other relevant information, and save the data in a structured format for further analysis.

### Features

- **Scrape Indeed**: Extract job listings from Indeed, including job title, company, location, and job description.
- **Scrape Bayt**: Extract job listings from Bayt with similar details.
- **Save Data**: Save the scraped data into CSV files for easy access and analysis.

### Requirements

- Python 3.x
- BeautifulSoup
- Requests
- Pandas

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web-scrapping.git
   ```
2. Navigate to the project directory:
   ```bash
   cd web-scrapping
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Scraping Indeed**:
   - Run the `indeed.py` script to start scraping job listings from Indeed.
     ```bash
     python indeed.py
     ```

2. **Scraping Bayt**:
   - Run the `bayt.py` script to start scraping job listings from Bayt.
     ```bash
     python bayt.py
     ```

3. **Data Output**:
   - The scraped data will be saved in CSV files named `indeed_jobs.csv` and `bayt_jobs.csv` respectively.

### Contribution

Feel free to fork this repository, create a branch, and submit pull requests. Any improvements or bug fixes are welcome!

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

Happy scraping!
