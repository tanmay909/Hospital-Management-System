### **Project Summary: Hospital Management System (Python, Tkinter, MySQL)**

This project is a **Hospital Management System** built with **Python’s Tkinter library** for the GUI and **MySQL database** for data storage. The system allows entry, storage, update, deletion, and display of patient prescription records.

---

### **Key Features:**

1. **Graphical User Interface (GUI):**

   * Created using **Tkinter** with multiple frames:

     * **Patient Information Form** (data entry fields).
     * **Prescription Display Panel** (text area to generate prescriptions).
     * **Button Panel** (for CRUD operations).
     * **Details Table** (shows all patient records with scrollbars).

2. **Patient & Prescription Data Handling:**

   * Fields include tablet name, reference number, dosage, number of tablets, lot number, issue & expiry dates, daily dose, side effects, blood pressure, storage advice, NHS number, patient details (name, DOB, address).
   * Data entered in the form is saved into the **MySQL database** (`hospital` table).

3. **Core Functionalities:**

   * **Add Prescription Data** (`iPrescriptionData`): Inserts new records into MySQL.
   * **Update Record** (`iupdate`): Edits patient data based on reference number.
   * **Delete Record** (`idelete`): Removes records by reference number.
   * **Fetch & Display** (`fetch_data`): Loads records into a Treeview table.
   * **Generate Prescription** (`iPrescription`): Produces a formatted prescription in the text area.
   * **Clear Form** (`clear`): Resets all fields and clears prescription box.
   * **Exit Program** (`exit`): Exits after confirmation.

4. **Database Integration:**

   * Uses **MySQL Connector** to connect with a database named `Tann`.
   * Performs SQL operations (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) on the `hospital` table.

5. **Interactive Table (Treeview):**

   * Displays all patient records in a structured format.
   * Allows record selection, which auto-fills the data entry form.

---

### **Technologies Used:**

* **Python** (Tkinter for GUI, MySQL Connector for database interaction).
* **MySQL** (data storage for patient and prescription details).
* **OOP Concepts** (Hospital class encapsulating all logic).

---

### **Purpose & Application:**

The system is designed to **manage patient prescription records efficiently** in a hospital or clinic setting. It provides:

* Easy data entry and retrieval.
* Record updating and deletion.
* Auto-generated prescription notes.
* A clean GUI for hospital staff.

