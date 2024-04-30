## Flask Application Design

**HTML Files:**

- `index.html`:
  - Main landing page of the application.
  - Includes information about the loyalty program and its benefits.
  - Links to pages for earning and spending points.

- `earn_points.html`:
  - Displays various ways to earn loyalty points.
  - Includes fields for entering relevant information (e.g., years of membership, top-up percentage).

- `spend_points.html`:
  - Lists available options for spending loyalty points.
  - Includes fields for selecting the desired option and entering relevant details (e.g., amount of points to redeem).

**Routes:**

- `/earn_points`:
  - Handles requests to the `earn_points.html` page.
  - Calculates and displays the number of points earned based on the submitted information.

- `/spend_points`:
  - Handles requests to the `spend_points.html` page.
  - Deducts the corresponding number of points from the user's balance based on the selected option and entered details.

- `/program_details`:
  - Displays a detailed description of the loyalty program, including earning and spending rules, benefits, and drawbacks.

- `/report`:
  - Generates a report containing insights into the program's customer satisfaction, revenue generation, and operational costs.